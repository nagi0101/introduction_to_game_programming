import pygame
import sys
from Player import Player

class Game:
    _instance = None
    done = False
    game_objects = []
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Game, cls).__new__(cls)
        return cls._instance

    def run(self):
        self.init()

        # Main game loop
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  # end game when 'q' is pressed
                        self.done = True

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.player.move(dx=-5)
            if keys[pygame.K_RIGHT]:
                self.player.move(dx=5)
            if keys[pygame.K_UP]:
                self.player.move(dy=-5)
            if keys[pygame.K_DOWN]:
                self.player.move(dy=5)

            # --- Drawing code should go here
            self.screen.fill((0, 0, 0))  # fill the screen with black
            pygame.draw.rect(self.screen, (255, 255, 255), self.player.rect)  # draw player

            # --- Go ahead and update the screen with what we've drawn
            pygame.display.flip()
        
        self.exit_game()

    def exit_game(self):
        # Close the window and quit.
        pygame.quit()
        sys.exit()

    def append_game_object(self, object):
        self.game_objects.append(object)
        object.game = self

    def init(self):
        pygame.init()

        # Set the size of the window
        size = (700, 500)
        self.screen = pygame.display.set_mode(size)

        # Set title of the window
        pygame.display.set_caption("My Pygame Window")

        # Create a player and an enemy
        self.player = Player(50, 50, 64, 64)

        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()
        # --- Limit to 60 frames per second
        self.clock.tick(60)

    def update(self):
        for game_object in self.game_objects:
            game_object.tick()
    
    def render(self):
        ""