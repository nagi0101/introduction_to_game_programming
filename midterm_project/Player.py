import pygame

from GameObject import GameObject
from Utils.Vector import Vec3
from Components.MovementComponent import MovementComponent


class Player(GameObject):
    def __init__(self):
        self.add_component(MovementComponent(speed=5.0))
        self.rect = pygame.Rect(
            self.transform.translate.x,
            self.transform.translate.y,
            50, 50)
        
    def tick(self, deltatime):        
        self.rect.x = self.transform.translate.x
        self.rect.y = self.transform.translate.y
        pygame.draw.rect(self.game.screen, (255, 255, 255), self.rect)
        
        super().tick(deltatime)