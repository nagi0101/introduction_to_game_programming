import pygame

from GameObject import GameObject

class Player(GameObject):
    def __init__(self, x, y, w, h, speed=(0,0)):
        self.rect = pygame.Rect(x, y, w, h)
        self.speed = speed

    def tick(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move(dx=-1)
        if keys[pygame.K_RIGHT]:
            self.move(dx=1)
        if keys[pygame.K_UP]:
            self.move(dy=-1)
        if keys[pygame.K_DOWN]:
            self.move(dy=1)
            
        self.rect.x = self.transform.translate.x
        self.rect.y = self.transform.translate.y
        
        pygame.draw.rect(self.game.screen, (255, 255, 255), self.rect)
        
        super().tick()

    def move(self, dx=0, dy=0):
        self.transform.translate.x += dx
        self.transform.translate.y += dy
