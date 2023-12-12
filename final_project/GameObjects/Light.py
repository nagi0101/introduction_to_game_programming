from math import pi

import pygame

from GameObjects.GameObject import GameObject

from Utils.Transform import Transform
from Utils.Vector import Vec3

from Components.LightComponent import LightComponent

class Light(GameObject):
    def __init__(self, transform:Transform=Transform(), strength:Vec3=Vec3.from_scalar(1),
                 falloffStart:float=0.0, falloffEnd:float=1.0) -> None:
        super().__init__(transform)
        self.light_comp = LightComponent(
            transform=transform,
            strength=strength,
            falloffStart=falloffStart,
            falloffEnd=falloffEnd
            )
        self.add_component(self.light_comp)
    
    def update(self, deltatime):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.light_comp.transform.rotate.yaw += 0.5 * pi * deltatime
        elif keys[pygame.K_RIGHT]:
            self.light_comp.transform.rotate.yaw -= 0.5 * pi * deltatime    
        
        super().update(deltatime)