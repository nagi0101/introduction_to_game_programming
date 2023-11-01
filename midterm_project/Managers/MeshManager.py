from OpenGL.GL import *

from Utils.Singleton import Singleton
from Utils.Vector import Vec3

from Components.MeshComponent import MeshComponent, Vertex


class MeshManager(metaclass=Singleton):
    class Factory(metaclass=Singleton):
        @classmethod
        def box(self, scale:float = 1.0) -> MeshComponent:
            vertices= [
                # Up
                Vertex(position=Vec3(1, 1, 1) * scale, color=Vec3(1.0, 0.0, 0.0)),
                Vertex(position=Vec3(1, 1, -1) * scale, color=Vec3(1.0, 0.0, 0.0)),
                Vertex(position=Vec3(-1, 1, -1) * scale, color=Vec3(1.0, 0.0, 0.0)),
                Vertex(position=Vec3(-1, 1, 1) * scale, color=Vec3(1.0, 0.0, 0.0)),

                #Down
                Vertex(position=Vec3(-1, -1, -1) * scale, color=Vec3(0.0, 1.0, 0.0)),
                Vertex(position=Vec3(1, -1, -1) * scale, color=Vec3(0.0, 1.0, 0.0)),
                Vertex(position=Vec3(1, -1, 1) * scale, color=Vec3(0.0, 1.0, 0.0)),
                Vertex(position=Vec3(-1, -1, 1) * scale, color=Vec3(0.0, 1.0, 0.0)),

                #Front
                Vertex(position=Vec3(-1, 1, 1) * scale, color=Vec3(0.0, 0.0, 1.0)),
                Vertex(position=Vec3(-1, -1, 1) * scale, color=Vec3(0.0, 0.0, 1.0)),
                Vertex(position=Vec3(1, -1, 1) * scale, color=Vec3(0.0, 0.0, 1.0)),
                Vertex(position=Vec3(1, 1, 1) * scale, color=Vec3(0.0, 0.0, 1.0)),

                #Back
                Vertex(position=Vec3(1, -1, -1) * scale, color=Vec3(1.0, 1.0, 0.0)),
                Vertex(position=Vec3(-1, -1, -1) * scale, color=Vec3(1.0, 1.0, 0.0)),
                Vertex(position=Vec3(-1, 1, -1) * scale, color=Vec3(1.0, 1.0, 0.0)),
                Vertex(position=Vec3(1, 1, -1) * scale, color=Vec3(1.0, 1.0, 0.0)),

                #Right
                Vertex(position=Vec3(1, 1, 1) * scale, color=Vec3(1.0, 0.0, 1.0)),
                Vertex(position=Vec3(1, -1, 1) * scale, color=Vec3(1.0, 0.0, 1.0)),
                Vertex(position=Vec3(1, -1, -1) * scale, color=Vec3(1.0, 0.0, 1.0)),
                Vertex(position=Vec3(1, 1, -1) * scale, color=Vec3(1.0, 0.0, 1.0)),

                #Left
                Vertex(position=Vec3(-1, 1, -1) * scale, color=Vec3(0.0, 1.0, 1.0)),
                Vertex(position=Vec3(-1, -1, -1) * scale, color=Vec3(0.0, 1.0, 1.0)),
                Vertex(position=Vec3(-1, -1, 1) * scale, color=Vec3(0.0, 1.0, 1.0)),
                Vertex(position=Vec3(-1, 1, 1) * scale, color=Vec3(0.0, 1.0, 1.0)),
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