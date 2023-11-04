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
        self.box = MeshManager().Factory.box(
            transform=Transform(
                translate=Vec3(0, 0, 0),
                rotate=Rot3()
            ))
        self.add_component(MovementComponent(speed=5.0))
        self.add_component(self.box)

    def update(self, deltatime):
        super().update(deltatime)
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            pass
            # print("pressed")
            # glRotatef(0.5 * pi * TimeManager().delta_second, 1, 0, 0)
        # self.box.transform.rotate.roll += 0.05 * pi * TimeManager().delta_second
        # self.box.transform.translate.z = 5 * cos(time())