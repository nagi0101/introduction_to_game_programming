import pygame
import OpenGL
if __debug__:
    OpenGL.ERROR_LOGGING = True
else:
    OpenGL.ERROR_LOGGING = False
from OpenGL.GL import *
from OpenGL.GLU import *

import numpy as np

from Utils.Singleton import Singleton

from Managers.TimeManager import TimeManager
from Managers.MeshManager import MeshManager

class RenderManager(metaclass=Singleton):
    _game=None
    _screen=pygame.Surface

    def __init__(self, game) -> None:
        self._game = game
        self.display = (800, 600)
        self._screen = pygame.display.set_mode(self.display, pygame.DOUBLEBUF|pygame.OPENGL)
        gluPerspective(45, (self.display[0]/self.display[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)

    def draw(self) -> None:
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glRotatef(1 * TimeManager().delta_second, 3, 1, 1)
        cube = MeshManager.Factory.line_box(2)
        cube.draw()
        pygame.display.flip()

    @property
    def screen(self) -> None:
        return self.screen
    @screen.setter
    def screen(self, screen:pygame.Surface):
        self._screen = screen

    