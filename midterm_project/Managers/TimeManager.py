import pygame
import time

from Utils.Singleton import Singleton

class TimeManager(metaclass=Singleton):
    _clock: pygame.time.Clock = None
    _game = None
    time:float
    fixed_time:float
    fixed_delta_second:float
    delta_second:float
    accumulator:float
    
    def update(self) -> None:
        pass
    
    def fixed_update(self) -> None:
        pass

    def must_update(self) -> bool:
        return self.accumulator >= self.fixed_delta_second

    def __init__(self, game) -> None:
        self._game = game
        self._clock = pygame.time.Clock()
        self.initialize_time_data()

    @property
    def framerate(self) -> int:
        return self._clock.tick()
    @framerate.setter
    def framerate(self, framerate:float):
        self._clock.tick(framerate)
    
    def initialize_time_data(self) -> None:
        self.time = time.time()
        self.fixed_time = self.time
        self.accumulator = 0.0
    
    @property
    def interpolation_alpha(self) -> float:
        return (self.time - self.fixed_time) / self.fixed_delta_second