import pygame

from Utils.Singleton import Singleton

class TimeManager(metaclass=Singleton):
    _clock: pygame.time.Clock = None
    _game = None
    time:float = 0.0
    fixed_time:float = 0.0
    fixed_delta_second:float = 0.0
    delta_second:float = 0.0
    accumulator:float = 0.0
    
    def update(self) -> None:
        pass
    
    def fixed_update(self) -> None:
        pass

    def must_update(self) -> bool:
        return self.accumulator >= self.fixed_delta_second

    def __init__(self, game) -> None:
        self._game = game
        self._clock = pygame.time.Clock()

    @property
    def framerate(self) -> int:
        return self._clock.tick()
    @framerate.setter
    def framerate(self, framerate:float):
        self._clock.tick(framerate)