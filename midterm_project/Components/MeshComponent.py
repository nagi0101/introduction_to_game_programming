import OpenGL
if __debug__:
    OpenGL.ERROR_LOGGING = True
else:
    OpenGL.ERROR_LOGGING = False
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

from Components.BaseComponents import BaseComponents

class MeshComponent(BaseComponents):
    _vertices: np.ndarray
    _edges: np.ndarray
    _primitive_type: Constant

    def __init__(self, vertices, edges, primitive_type) -> None:
        super().__init__()
        self._vertices = vertices
        self._edges = edges
        self._primitive_type = primitive_type
    
    def draw(self) -> None:
        glBegin(self._primitive_type)
        for edge in self._edges:
            for vertex in edge:
                glVertex3fv(self._vertices[vertex])
        glEnd()