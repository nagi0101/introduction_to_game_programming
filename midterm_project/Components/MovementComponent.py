from math import pi

import pygame

from Components.BaseComponents import BaseComponents

from Utils.Vector import Vec3

from Managers.TimeManager import TimeManager

class MovementComponent(BaseComponents):
    speed:float
    
    def __init__(self, speed:float) -> None:
        super().__init__()
        self.speed = speed
        
    def update(self, deltatime:float):
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
        ds = self.owner_object.transform.rotate.rotate_vec3(Vec3(dx, 0, dz)) * deltatime
        
        map_data = self.owner_object.game.map.map_data
        max_z, max_x = len(map_data) - 1, len(map_data[0]) - 1
        new_pos = self.owner_object.transform.translate + ds
        idx_x, idx_z = int(new_pos.x), int(new_pos.z)
        
        if map_data[idx_z][idx_x] != 0:
            x = max(1, min(self.owner_object.transform.translate.x, max_x))
            new_pos.x = x
        
        if map_data[idx_z][idx_x] != 0:
            z = max(1, min(self.owner_object.transform.translate.z, max_z))
            new_pos.z = z
            
        self.owner_object.transform.translate = new_pos
        
        if keys[pygame.K_LEFT]:
            self.owner_object.transform.rotate.yaw += 0.5 * pi * TimeManager().delta_second
        elif keys[pygame.K_RIGHT]:
            self.owner_object.transform.rotate.yaw -= 0.5 * pi * TimeManager().delta_second
            
        
        super().update(deltatime)