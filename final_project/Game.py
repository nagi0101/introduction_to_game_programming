import sys
import time
from typing import List
from math import pi, cos, sin

import pygame

from Utils.Singleton import Singleton
from Utils.Transform import Transform
from Utils.Vector import Vec3
from Utils.Rotator import Rot3

from GameObjects.GameObject import GameObject
from GameObjects.Player import Player
from GameObjects.CollidableBox import CollidableBox

from Managers.EventManager import EventManager
from Managers.TimeManager import TimeManager
from Managers.RenderManager import RenderManager

from Components.MeshComponent import MeshComponent
from Components.LightComponent import LightComponent
    
class Game(metaclass=Singleton):
    done:bool = False
    game_objects:List[GameObject] = []

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("My Pygame Window")

        TimeManager(self)
        TimeManager().fixed_delta_second = 1 / 20
        TimeManager().framerate = 0
        
        EventManager(self)
        EventManager().add_handler(pygame.QUIT, self.handle_exit)
        EventManager().add_handler(pygame.KEYDOWN, self.handle_exit)

        RenderManager(self)

        self.player=Player(transform=Transform(
            translate=Vec3(0, 0, 0),
            rotate=Rot3(0, 0, 0)
        ))
        self.append_game_object(self.player)
        
        N = 8
        dtheta = 2 * pi / N
        d = 5
        for i in range(N):
            x = d * cos(dtheta * i)
            z = d * sin(dtheta * i)
            self.append_game_object(CollidableBox(transform=Transform(
                    translate=Vec3(x, 0, z),
                    scale=Vec3.from_scalar(d)), 
                    texture_path="Resources\Textures\\blocks1.jpg"))
            
        LightComponent(
            transform=Transform(
                translate=Vec3(0, 0, 0),
                rotate=Rot3(0.0, 0.0, 0.0)),
            strength=Vec3(1.0, 1.0, 1.0),
            falloffStart=1, falloffEnd=10)
    
        
        # self.append_game_object(Cubemap())

    def run(self):
        TimeManager().initialize_time_data()
        while not self.done:
            while(TimeManager().must_update()):
                TimeManager().fixed_time = time.time()
                TimeManager().accumulator -= TimeManager().fixed_delta_second
                for object in self.game_objects:
                    object.fixed_update(TimeManager().fixed_delta_second)
            
            TimeManager().delta_second = time.time() - TimeManager().time
            TimeManager().time = time.time()
            TimeManager().accumulator += TimeManager().delta_second

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

    def append_game_object(self, object:GameObject):
        self.game_objects.append(object)
        object.game = self

    def remove_game_object(self, object:GameObject):
        for component in object.components:
            if isinstance(component, MeshComponent):
                RenderManager().remove_mesh(component)
        self.game_objects.remove(object)