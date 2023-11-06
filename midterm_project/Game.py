import pygame
import sys
from typing import List 

from Utils.Singleton import Singleton
from Utils.Transform import Transform
from Utils.Vector import Vec3
from Utils.Rotator import Rot3

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
        
        self.player=Player(transform=Transform(
            translate=Vec3(1.5, 0, 1.5),
            rotate=Rot3(0, 0, -2)
        ))
        self.append_game_object(self.player)
        self.map = Map()
        self.append_game_object(self.map)

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

