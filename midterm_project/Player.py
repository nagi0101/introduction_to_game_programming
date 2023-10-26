from GameObject import GameObject
import pygame

class Player(GameObject):
    def __init__(self, x, y, w, h, speed=(0,0)):
        self.rect = pygame.Rect(x, y, w, h)
        self.speed = speed

    def move(self, dx=0, dy=0):
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy