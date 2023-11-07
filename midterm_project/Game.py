import sys
import time
from typing import List
from random import sample

import pygame

from Utils.Singleton import Singleton
from Utils.Transform import Transform
from Utils.Vector import Vec3
from Utils.Rotator import Rot3

from GameObjects.GameObject import GameObject
from GameObjects.Player import Player
from GameObjects.Map import Map
from GameObjects.CollidableBox import CollidableBox

from Managers.EventManager import EventManager
from Managers.TimeManager import TimeManager
from Managers.RenderManager import RenderManager

from Components.MeshComponent import MeshComponent
    
class Game(metaclass=Singleton):
    done:bool = False
    clear:bool = False
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
        
        self.map = Map()
        self.append_game_object(self.map)

        self.player=Player(transform=Transform(
            translate=Vec3(1.5, 0, 1.5),
            rotate=Rot3(0, 0, -2)
        ))
        self.append_game_object(self.player)

        
        
        COLLIDE_NUM = 5
        empty_positions = sample(self.map.get_empty_pos(), COLLIDE_NUM)
        for pos in empty_positions:
            self.append_game_object(CollidableBox(transform=Transform(
                translate=pos,
                scale=Vec3.from_scalar(0.5)
            ), threshold=0.2))

    def run(self):
        self.start_time = time.time()
        self.clear_time = 0
        while not self.done:
            EventManager().consume_events()
            if self.clear:
                RenderManager().draw_gameover(self.clear_time)
                continue
            
            for object in self.game_objects:
                object.update(TimeManager().delta_second)
            
            RenderManager().draw()
        
        self.exit_game()
    
    def clear_game(self):
        self.clear = True
        self.clear_time = time.time() - self.start_time
        
    def handle_exit(self, e:pygame.event.Event):
        if(e.type == pygame.QUIT or e.key == pygame.K_q):
            self.done = True

    def exit_game(self):
        pygame.quit()
        sys.exit()

    def append_game_object(self, object:GameObject):
        self.game_objects.append(object)
        object.game = self

    def remove_game_object(self, object:GameObject):
        for component in object.components:
            if isinstance(component, MeshComponent):
                RenderManager().remove_mesh(component)
        self.game_objects.remove(object)