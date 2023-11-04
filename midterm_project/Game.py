import pygame
import sys
from typing import List 

from Utils.Singleton import Singleton

from GameObjects.GameObject import GameObject
from GameObjects.Player import Player
from GameObjects.Map import Map

from Managers.EventManager import EventManager
from Managers.TimeManager import TimeManager
from Managers.RenderManager import RenderManager

class Game(metaclass=Singleton):
    done = False
    game_objects:List[GameObject] = []

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("My Pygame Window")

        TimeManager(self)
        TimeManager().framerate = 60
        
        EventManager(self)
        EventManager().add_handler(pygame.QUIT, self.handle_exit)
        EventManager().add_handler(pygame.KEYDOWN, self.handle_exit)

        RenderManager(self)
        
        self.append_game_object(Player())
        self.append_game_object(Map())

    def run(self):
        while not self.done:
            EventManager().consume_events()
            
            for object in self.game_objects:
                object.update(TimeManager().delta_second)
            
            RenderManager().draw()
        
        self.exit_game()
        
    def handle_exit(self, e:pygame.event.Event):
        if(e.type == pygame.QUIT or e.key == pygame.K_q):
            self.done = True

    def exit_game(self):
        pygame.quit()
        sys.exit()

    def append_game_object(self, object):
        self.game_objects.append(object)
        object.game = self

