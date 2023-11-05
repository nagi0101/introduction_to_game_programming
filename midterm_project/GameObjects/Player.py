from math import cos, pi
from time import time

import pygame
import OpenGL
if __debug__:
    OpenGL.ERROR_LOGGING = True
else:
    OpenGL.ERROR_LOGGING = False
from OpenGL.GL import *
from OpenGL.GLU import *

from GameObjects.GameObject import GameObject

from Components.MovementComponent import MovementComponent
from Managers.MeshManager import MeshManager
from Managers.TimeManager import TimeManager

from Utils.Vector import Vec3
from Utils.Rotator import Rot3
from Utils.Transform import Transform

class Player(GameObject):
    def __init__(self) -> None:
        super().__init__()
        self.add_component(MovementComponent(speed=5.0))
        # self.add_component(MeshManager().Factory.box(
        #     transform=Transform(
        #         translate=Vec3(0, 0, 0),
        #         rotate=Rot3()
        #     )))

    def update(self, deltatime):
        super().update(deltatime)
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            glRotatef(pi * 10 * TimeManager().delta_second, 1, 0, 0)
        if pygame.key.get_pressed()[pygame.K_UP]:
            glRotatef(-pi * 10 * TimeManager().delta_second, 1, 0, 0)
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            glTranslatef(0.0, -5.0 * TimeManager().delta_second, 0.0)
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            glTranslatef(0.0, 5.0 * TimeManager().delta_second, 0.0)