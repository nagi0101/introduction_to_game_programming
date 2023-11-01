import numpy as np

from OpenGL.GL import *

from Utils.Singleton import Singleton
from Utils.Vector import Vec3

from Components.MeshComponent import MeshComponent, Vertex


class MeshManager(metaclass=Singleton):
    class Factory(metaclass=Singleton):
        @classmethod
        def line_box(self, scale:float) -> MeshComponent:
            vertices= [
                Vertex(position=Vec3(1, -1, -1) * scale),
                Vertex(position=Vec3(1, 1, -1) * scale),
                Vertex(position=Vec3(-1, 1, -1) * scale),
                Vertex(position=Vec3(-1, -1, -1) * scale),
                Vertex(position=Vec3(1, -1, 1) * scale),
                Vertex(position=Vec3(1, 1, 1) * scale),
                Vertex(position=Vec3(-1, -1, 1) * scale),
                Vertex(position=Vec3(-1, 1, 1) * scale)
            ]
            indices = (
                0,1,
                0,3,
                0,4,
                2,1,
                2,3,
                2,7,
                6,3,
                6,4,
                6,7,
                5,1,
                5,4,
                5,7
                )
            return MeshComponent(vertices, indices, GL_LINES)