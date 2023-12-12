from math import pi
from copy import deepcopy

import pygame

from Components.BaseComponents import BaseComponents

from Managers.TimeManager import TimeManager

from Utils.Vector import Vec3
from Utils.Transform import Transform


class MovementComponent(BaseComponents):
    speed:float
    fixed_transform_last:Transform
    fixed_transform_now:Transform
    
    def __init__(self, speed:float) -> None:
        super().__init__()
        self.speed = speed
        self.fixed_transform_last = Transform()
        self.fixed_transform_now = Transform()
    
    def on_attached(self) -> None:
        self.fixed_transform_last = self.owner_object.transform
        self.fixed_transform_now = deepcopy(self.fixed_transform_last)
        
        super().on_attached()
    
    def update(self, deltatime:float):
        alpha = TimeManager().interpolation_alpha
        interpolated_transform = Transform.lerp(
            self.fixed_transform_last, 
            self.fixed_transform_now, 
            alpha
            )
        self.owner_object.transform = interpolated_transform
        
        super().update(deltatime)
        
    def fixed_update(self, fixed_deltatime: float) -> None:
        new_transform = deepcopy(self.fixed_transform_now)
        self.fixed_transform_last = deepcopy(self.fixed_transform_now)
        
        keys = pygame.key.get_pressed()
        
        dx, dz = 0, 0
        if keys[pygame.K_a]:
            dx += -self.speed
        elif keys[pygame.K_d]:
            dx += self.speed
        
        if keys[pygame.K_w]:
            dz += -self.speed
        elif keys[pygame.K_s]:
            dz += self.speed
        ds = new_transform.rotate.rotate_vec3(Vec3(dx, 0, dz)) * fixed_deltatime
        
        new_transform.translate = new_transform.translate + ds
        
        
        pygame.event.set_grab(True)
        rel = pygame.mouse.get_rel()
        pygame.mouse.set_pos = (400, 300)
        new_transform.rotate.yaw -= rel[0] * pi * 0.1 * fixed_deltatime
        new_transform.rotate.pitch -= rel[1] * pi * 0.1 * fixed_deltatime
        
        self.fixed_transform_now = new_transform
        
        super().fixed_update(fixed_deltatime)