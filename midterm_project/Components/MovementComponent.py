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
        
        map_data = self.owner_object.game.map.map_data
        max_z, max_x = len(map_data) - 1, len(map_data[0]) - 1
        new_pos = new_transform.translate + ds
        idx_x, idx_z = max(0, min(int(new_pos.x), max_x)), max(0, min(int(new_pos.z), max_z))
        
        if map_data[idx_z][idx_x] != 0:
            x = max(1, min(new_transform.translate.x, max_x))
            new_pos.x = x
        
        if map_data[idx_z][idx_x] != 0:
            z = max(1, min(new_transform.translate.z, max_z))
            new_pos.z = z
        new_transform.translate = new_pos
        
        if keys[pygame.K_LEFT]:
            new_transform.rotate.yaw += 0.5 * pi * fixed_deltatime
        elif keys[pygame.K_RIGHT]:
            new_transform.rotate.yaw -= 0.5 * pi * fixed_deltatime
        
        self.fixed_transform_now = new_transform
        
        super().fixed_update(fixed_deltatime)