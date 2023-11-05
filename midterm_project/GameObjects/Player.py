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
from Components.CameraComponent import CameraComponent

from Managers.MeshManager import MeshManager
from Managers.TimeManager import TimeManager

from Utils.Vector import Vec3
from Utils.Rotator import Rot3
from Utils.Transform import Transform

class Player(GameObject):
    def __init__(self) -> None:
        super().__init__()
        self.camera = CameraComponent()
        self.add_component(self.camera)
        self.add_component(MovementComponent(speed=5.0))

    def update(self, deltatime):
        super().update(deltatime)
        if pygame.key.get_pressed()[pygame.K_w]:
            self.transform.translate += self.transform.get_forward_vector() * TimeManager().delta_second
        elif pygame.key.get_pressed()[pygame.K_s]:
            self.transform.translate += -self.transform.get_forward_vector() * TimeManager().delta_second
        
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.transform.rotate.yaw += 0.5 * pi * TimeManager().delta_second
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.transform.rotate.yaw -= 0.5 * pi * TimeManager().delta_second