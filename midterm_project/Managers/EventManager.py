import pygame
from typing import Callable, List, Dict

from Utils.Singleton import Singleton

class EventManager(metaclass=Singleton):
    game = None
    
    _handlers:Dict[int, List[Callable]] = {}
    
    def __init__(self, game) -> None:
        self.game = game
        
    def add_handler(self, event:int, handler:Callable):
        if event not in self._handlers.keys():
            self._handlers[event] = []
        self._handlers[event].append(handler)
    
    def tick(self):
        for event in pygame.event.get():
            if event.type in self._handlers.keys():
                for handler in self._handlers[event.type]:
                    handler(event)
                
            if event.type == pygame.QUIT:
                self.game.done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:  # end game when 'q' is pressed
                    self.game.done = True