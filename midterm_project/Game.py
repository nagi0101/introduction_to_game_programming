import pygame
import sys

from Utils.Singleton import Singleton
from Player import Player
from Managers.EventManager import EventManager

class Game(metaclass=Singleton):
    done = False
    game_objects = []

    def run(self):
        self.init()

        # Main game loop
        while not self.done:
            EventManager().tick()

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
        
    def set_exit_flag(self, flag:bool):
        self.done = flag

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

        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        
        EventManager(self)
        EventManager().add_handler(pygame.QUIT, lambda: self.set_exit_flag(True))

    def update(self):
        for game_object in self.game_objects:
            game_object.tick()
    
    def render(self):
        ""