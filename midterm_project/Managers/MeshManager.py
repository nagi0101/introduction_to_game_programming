import numpy as np

from OpenGL.GL import *

from Utils.Singleton import Singleton
from Utils.Vector import Vec3

from Components.MeshComponent import MeshComponent, Vertex


class MeshManager(metaclass=Singleton):
    class Factory(metaclass=Singleton):
        @classmethod
        def line_box(self, scale:float = 1.0) -> MeshComponent:
            vertices= [
                # Up
                Vertex(position=Vec3(1, 1, 1) * scale),
                Vertex(position=Vec3(1, 1, -1) * scale),
                Vertex(position=Vec3(-1, 1, -1) * scale),
                Vertex(position=Vec3(-1, 1, 1) * scale),

                #Down
                Vertex(position=Vec3(-1, -1, -1) * scale),
                Vertex(position=Vec3(1, -1, -1) * scale),
                Vertex(position=Vec3(1, -1, 1) * scale),
                Vertex(position=Vec3(-1, -1, 1) * scale),

                #Front
                Vertex(position=Vec3(-1, 1, 1) * scale),
                Vertex(position=Vec3(-1, -1, 1) * scale),
                Vertex(position=Vec3(1, -1, 1) * scale),
                Vertex(position=Vec3(1, 1, 1) * scale),
                
                #Back
                Vertex(position=Vec3(1, -1, -1) * scale),
                Vertex(position=Vec3(1, 1, -1) * scale),
                Vertex(position=Vec3(-1, 1, -1) * scale),
                Vertex(position=Vec3(-1, -1, -1) * scale),

                #Right
                Vertex(position=Vec3(1, 1, 1) * scale),
                Vertex(position=Vec3(1, -1, 1) * scale),
                Vertex(position=Vec3(1, -1, -1) * scale),
                Vertex(position=Vec3(1, 1, -1) * scale),
                
                #Left
                Vertex(position=Vec3(-1, 1, -1) * scale),
                Vertex(position=Vec3(-1, -1, -1) * scale),
                Vertex(position=Vec3(-1, -1, 1) * scale),
                Vertex(position=Vec3(-1, 1, 1) * scale),
            ]
            indices = (
                0, 1, 2, 0, 2, 3,
                4, 5, 6, 4, 6, 7,
                8, 9, 10, 8, 10, 11,
                12, 13, 14, 12, 14, 15,
                16, 17, 18, 16, 18, 19,
                20, 21, 22, 20, 22, 23
                )
            return MeshComponent(vertices, indices, GL_TRIANGLES)