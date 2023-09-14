import pygame
import time
import random
from math import sqrt

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 640, 480
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE=(255, 165, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
NAVY = (0, 0, 128)
PURPLE = (128, 0, 128)
RAINBOW = [RED, ORANGE, YELLOW, GREEN, BLUE, NAVY, PURPLE]


# Snake and food properties
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [
    random.randrange(1, (WIDTH//10)) * 10, 
    random.randrange(1, (HEIGHT//10)) * 10
    ]
food_spawn = True
score_per_food = 1

# Direction
direction = 'RIGHT'
change_to = direction

# Initial frame rate
framerate = 15

# Score
score = 0
highscore = score

# Fever mode
is_fever = False
fever_length = 5
fever_score_scale = 1.5
fever_framerate_scale = 2
fever_pos = [
    random.randrange(1, (WIDTH//10)) * 10, 
    random.randrange(1, (HEIGHT//10)) * 10
    ]
fever_spawn = True
fever_start = time.time()

# Dead
is_dead = False
dead_effect_length = 1.5
last_dead = time.time()

def render_fever_background():
    pixel_size = 40
    center_pos = (WIDTH // 2, HEIGHT // 2)
    for y in range(0, HEIGHT // pixel_size):
        for x in range(0, WIDTH // pixel_size):
            xpos = x * pixel_size
            ypos = y * pixel_size
            pixel_vec = [center_pos[0] - xpos, center_pos[1] - ypos]
            dist = sqrt(pixel_vec[0] ** 2 + pixel_vec[1] ** 2)
            wave_arg = dist / 1000 - time.time() / 2
            wave_zero_one = abs(wave_arg - int(wave_arg))
            index = int((abs((wave_zero_one - 0.5) * 12) + 0.5))
            pixel_color = RAINBOW[index]
            pygame.draw.rect(window, pixel_color, pygame.Rect(xpos, ypos, pixel_size, pixel_size))

# Display Score function
def Your_score(score, highscore):
    value = pygame.font.SysFont('comicsans', 30).render("Your Score: " + str(score), True, WHITE)
    window.blit(value, [0, 0])
    value = pygame.font.SysFont('comicsans', 30).render("Highscore: " + str(highscore), True, WHITE)
    window.blit(value, [0, 40])
    value = pygame.font.SysFont('comicsans', 30).render("Press c to continue", True, WHITE)
    window.blit(value, [0, HEIGHT - 40])
    
def initialize_game():
    global direction, change_to
    global snake_pos, snake_body
    global food_pos, food_spawn
    global score, framerate
    global is_fever, fever_length, fever_score_scale, fever_framerate_scale,\
        fever_pos, fever_spawn, fever_start
    global is_dead

    # Snake and food properties
    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]
    food_pos = [
        random.randrange(1, (WIDTH//10)) * 10, 
        random.randrange(1, (HEIGHT//10)) * 10
        ]
    food_spawn = True

    # Direction
    direction = 'RIGHT'
    change_to = direction

    # Initial frame rate
    framerate = 15

    # Score
    score = 0

    # Fever mode
    is_fever = False
    fever_length = 5
    fever_score_scale = 1.5
    fever_framerate_scale = 2
    fever_pos = [
        random.randrange(1, (WIDTH//10)) * 10, 
        random.randrange(1, (HEIGHT//10)) * 10
        ]
    fever_spawn = True
    
    # Dead
    is_dead = False
    
def spawn_fever():
    global fever_spawn, fever_pos
    
    fever_pos = [
        random.randrange(1, (WIDTH//10)) * 10, 
        random.randrange(1, (HEIGHT//10)) * 10
        ]
    fever_spawn = True

def render_snake(color):
    for pos in snake_body:
        pygame.draw.rect(window, color, pygame.Rect(pos[0], pos[1], 10, 10))

def render():
    window.fill(BLACK)
    if is_fever:
        render_fever_background()
    snake_color = BLACK if is_fever else GREEN
    render_snake(snake_color)
    if(food_spawn):
        food_color = BLACK if is_fever else RED
        pygame.draw.rect(window, food_color, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    if(fever_spawn):
        pygame.draw.rect(window, YELLOW, pygame.Rect(fever_pos[0], fever_pos[1], 10, 10))

    pygame.display.update()
    apply_framerate = framerate * fever_framerate_scale if is_fever else framerate
    pygame.time.Clock().tick(apply_framerate)

def dead():
    global is_dead, last_dead
    is_dead = True
    last_dead = time.time()
    
def check_dead():
    # Game Over conditions
    if snake_pos[0] < 0 or snake_pos[0] > WIDTH-10:
        dead()
        return
    if snake_pos[1] < 0 or snake_pos[1] > HEIGHT-10:
        dead()
        return
        
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            dead()
            return
            
# Main Function
def gameLoop():
    global direction, change_to
    global snake_pos, snake_body
    global food_pos, food_spawn, score_per_food
    global score, highscore, framerate
    
    global is_fever, fever_length, fever_score_scale, fever_framerate_scale,\
        fever_pos, fever_spawn, fever_start
    global is_dead, dead_effect_length, last_dead

    # Game Over
    game_over = False
    game_close = False

    while not game_over:
        if is_dead:
            while time.time() - last_dead < dead_effect_length:
                color = [BLACK, WHITE]
                i = int(time.time() * 2 - int(time.time() * 2) + 0.5)
                k = 1 - i
                window.fill(color[i])
                render_snake(color[k])
                pygame.display.update()
            game_close = True
            
        while game_close == True:
            highscore = max(highscore, score)
            window.fill(BLACK)
            Your_score(score, highscore)
            pygame.display.update()

            # Asking user to play again or quit
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        initialize_game()
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        # Validation of direction: avoid the overlap of snake's body
        if change_to == 'UP' and not direction == 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and not direction == 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and not direction == 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and not direction == 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10

        # Snake body growing mechanism: insert a new position (snake_pose) on 
        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            apply_score = score_per_food * fever_score_scale if is_fever else score_per_food
            score += apply_score
            framerate += 2
            food_spawn = False
            if not fever_spawn and not is_fever:
                spawn_fever()
        else:
            snake_body.pop()
            
        if fever_spawn and snake_pos[0] == fever_pos[0] and snake_pos[1] == fever_pos[1]:
            is_fever = True
            fever_spawn = False
            fever_start = time.time()

        if not food_spawn:
            food_pos = [
                random.randrange(1, (WIDTH//10)) * 10, 
                random.randrange(1, (HEIGHT//10)) * 10
                ]
            food_spawn = True
            
        if is_fever:
            if time.time() - fever_start > fever_length:
                is_fever = False

        check_dead()

        render()
        

    pygame.quit()
    quit()

# Run the game
gameLoop()