from typing import List

from OpenGL.GL import *

from Utils.Singleton import Singleton
from Utils.Vector import Vec3
from Utils.Rotator import Rot3
from Utils.Transform import Transform

from Components.MeshComponent import MeshComponent, Vertex


class MeshManager(metaclass=Singleton):
    class Factory(metaclass=Singleton):
        @classmethod
        def box(self, transform:Transform = Transform()) -> MeshComponent:
            vertices= [
                # Up
                Vertex(position=Vec3(1, 1, 1), color=Vec3(1.0, 0.0, 0.0)),
                Vertex(position=Vec3(1, 1, -1), color=Vec3(1.0, 0.0, 0.0)),
                Vertex(position=Vec3(-1, 1, -1), color=Vec3(1.0, 0.0, 0.0)),
                Vertex(position=Vec3(-1, 1, 1), color=Vec3(1.0, 0.0, 0.0)),

                #Down
                Vertex(position=Vec3(-1, -1, -1), color=Vec3(0.0, 1.0, 0.0)),
                Vertex(position=Vec3(1, -1, -1), color=Vec3(0.0, 1.0, 0.0)),
                Vertex(position=Vec3(1, -1, 1), color=Vec3(0.0, 1.0, 0.0)),
                Vertex(position=Vec3(-1, -1, 1), color=Vec3(0.0, 1.0, 0.0)),

                #Front
                Vertex(position=Vec3(-1, 1, 1), color=Vec3(0.0, 0.0, 1.0)),
                Vertex(position=Vec3(-1, -1, 1), color=Vec3(0.0, 0.0, 1.0)),
                Vertex(position=Vec3(1, -1, 1), color=Vec3(0.0, 0.0, 1.0)),
                Vertex(position=Vec3(1, 1, 1), color=Vec3(0.0, 0.0, 1.0)),

                #Back
                Vertex(position=Vec3(1, -1, -1), color=Vec3(1.0, 1.0, 0.0)),
                Vertex(position=Vec3(-1, -1, -1), color=Vec3(1.0, 1.0, 0.0)),
                Vertex(position=Vec3(-1, 1, -1), color=Vec3(1.0, 1.0, 0.0)),
                Vertex(position=Vec3(1, 1, -1), color=Vec3(1.0, 1.0, 0.0)),

                #Right
                Vertex(position=Vec3(1, 1, 1), color=Vec3(1.0, 0.0, 1.0)),
                Vertex(position=Vec3(1, -1, 1), color=Vec3(1.0, 0.0, 1.0)),
                Vertex(position=Vec3(1, -1, -1), color=Vec3(1.0, 0.0, 1.0)),
                Vertex(position=Vec3(1, 1, -1), color=Vec3(1.0, 0.0, 1.0)),

                #Left
                Vertex(position=Vec3(-1, 1, -1), color=Vec3(0.0, 1.0, 1.0)),
                Vertex(position=Vec3(-1, -1, -1), color=Vec3(0.0, 1.0, 1.0)),
                Vertex(position=Vec3(-1, -1, 1), color=Vec3(0.0, 1.0, 1.0)),
                Vertex(position=Vec3(-1, 1, 1), color=Vec3(0.0, 1.0, 1.0)),
            ]
            indices = (
                0, 1, 2, 0, 2, 3,
                4, 5, 6, 4, 6, 7,
                8, 9, 10, 8, 10, 11,
                12, 13, 14, 12, 14, 15,
                16, 17, 18, 16, 18, 19,
                20, 21, 22, 20, 22, 23
                )
            return MeshComponent(transform, vertices, indices, GL_TRIANGLES)
        
        @classmethod
        def from_map(cls, map) -> List[MeshComponent]:
            mesh_arr = []
            zmax = len(map)
            xmax = len(map[0])
            for idx_z, z in enumerate(map):
                for idx_x, x in enumerate(z):
                    if x == 0:
                        pass
                    elif x == 1:
                        transform = Transform(
                            translate=Vec3(idx_x - (xmax / 2), 0, idx_z - (zmax / 2)), 
                            scale=Vec3.from_scalar(0.5),
                            rotate=Rot3()
                            )
                        mesh_arr.append(cls.box(transform))
            return mesh_arr