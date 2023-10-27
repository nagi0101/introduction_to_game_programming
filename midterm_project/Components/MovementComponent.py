import pygame

from Components.BaseComponents import BaseComponents
from GameObject import GameObject

from Utils.Vector import Vec3

class MovementComponent(BaseComponents):
    speed:float
    
    def __init__(self, speed:float) -> None:
        super().__init__()
        self.speed = speed
        
    def tick(self, deltatime:float):
        dx, dy = 0, 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            dx += -self.speed
        elif keys[pygame.K_RIGHT]:
            dx += self.speed
        
        if keys[pygame.K_UP]:
            dy += -self.speed
        elif keys[pygame.K_DOWN]:
            dy += self.speed
        
        v = Vec3(dx, dy, 0)
        self.owner_object.transform.translate += v * deltatime
        
        super().tick(deltatime)