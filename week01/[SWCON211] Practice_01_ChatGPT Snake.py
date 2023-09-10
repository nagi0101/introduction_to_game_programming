import pygame
import time
import random

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
YELLOW = (255, 255, 0)

# Snake and food properties
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
food_spawn = True
score_per_food = 1

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
fever_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
fever_spawn = True
fever_start = time.time()


# Display Score function
def Your_score(score):
    value = pygame.font.SysFont('comicsans', 30).render("Your Score: " + str(score), True, WHITE)
    window.blit(value, [0, 0])
    
def initialize_game():
    global direction, change_to
    global snake_pos, snake_body
    global food_pos, food_spawn
    global score, framerate
    global is_fever, fever_length, fever_score_scale, fever_framerate_scale, fever_pos, fever_spawn, fever_start

    # Snake and food properties
    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]
    food_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
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
    fever_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
    fever_spawn = True
    
def spawn_fever():
    global fever_spawn, fever_pos
    
    fever_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
    fever_spawn = True

# Main Function
def gameLoop():
    global direction, change_to
    global snake_pos, snake_body
    global food_pos, food_spawn, score_per_food
    global score, framerate
    
    global is_fever, fever_length, fever_score_scale, fever_framerate_scale, fever_pos, fever_spawn, fever_start

    # Game Over
    game_over = False
    game_close = False

    while not game_over:
        while game_close == True:
            window.fill(BLACK)
            Your_score(score)
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
            
        if snake_pos[0] == fever_pos[0] and snake_pos[1] == fever_pos[1]:
            is_fever = True
            fever_spawn = False
            fever_start = time.time()

        if not food_spawn:
            food_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
            food_spawn = True
            
        if is_fever:
            if time.time() - fever_start > fever_length:
                is_fever = False

        window.fill(BLACK)
        for pos in snake_body:
            pygame.draw.rect(window, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
        if(food_spawn):
            pygame.draw.rect(window, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
        if(fever_spawn):
            pygame.draw.rect(window, YELLOW, pygame.Rect(fever_pos[0], fever_pos[1], 10, 10))

        # Game Over conditions
        if snake_pos[0] < 0 or snake_pos[0] > WIDTH-10:
            game_close = True
        if snake_pos[1] < 0 or snake_pos[1] > HEIGHT-10:
            game_close = True

        # Touching the snake body
        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_close = True

        pygame.display.update()
        # Limit frame rate to 15 Hz
        apply_framerate = framerate * fever_framerate_scale if is_fever else framerate
        pygame.time.Clock().tick(apply_framerate)

    pygame.quit()
    quit()

# Run the game
gameLoop()