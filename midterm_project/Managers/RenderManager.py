import pygame

from Utils.Singleton import Singleton

class RenderManager(metaclass=Singleton):
    _game=None
    _screen=pygame.Surface

    def __init__(self, game) -> None:
        self._game = game

    @property
    def screen(self) -> None:
        return self.screen
    @screen.setter
    def screen(self, screen:pygame.Surface):
        self._screen = screen

    