import pygame

from Utils.Singleton import Singleton

class TimeManager(metaclass=Singleton):
    _clock: pygame.time.Clock = None
    _game = None

    def __init__(self, game) -> None:
        self._game = game
        self._clock = pygame.time.Clock()

    @property
    def framerate(self) -> int:
        return self._clock.tick()
    @framerate.setter
    def framerate(self, framerate:float):
        self._clock.tick(framerate)

    @property
    def delta_second(self) -> float:
        return self._clock.get_time() / 1000