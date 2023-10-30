import pygame
import sys
from typing import List 

from Utils.Singleton import Singleton
from GameObject import GameObject
from Player import Player

from Managers.EventManager import EventManager
from Managers.TimeManager import TimeManager
from Managers.RenderManager import RenderManager

class Game(metaclass=Singleton):
    done = False
    game_objects:List[GameObject] = []

    def run(self):
        self.init()

        # Main game loop
        while not self.done:
            EventManager().tick()

            # --- Drawing code should go here
            self.screen.fill((0, 0, 0))  # fill the screen with black
            
            for object in self.game_objects:
                object.tick(TimeManager().delta_second)

            # --- Go ahead and update the screen with what we've drawn
            pygame.display.flip()
        
        self.exit_game()
        
    def handle_exit(self, e:pygame.event.Event):
        if(e.type == pygame.QUIT or e.key == pygame.K_q):
            self.done = True

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

        self.append_game_object(Player())

        TimeManager(self)
        TimeManager().framerate = 60
        
        EventManager(self)
        EventManager().add_handler(pygame.QUIT, self.handle_exit)
        EventManager().add_handler(pygame.KEYDOWN, self.handle_exit)

        RenderManager(self)


    def update(self):
        for game_object in self.game_objects:
            game_object.tick()
    
    def render(self):
        pass