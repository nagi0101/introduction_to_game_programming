from typing import List

import OpenGL
if __debug__:
    OpenGL.ERROR_LOGGING = True
else:
    OpenGL.ERROR_LOGGING = False
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np


from Components.BaseComponents import BaseComponents

from Utils.Vector import Vec3, Vec2

class Vertex:
    position:Vec3
    normal:Vec3
    color:Vec3
    texcoord:Vec2

    def __init__(self, position=Vec3(), normal=Vec3(), color=Vec3(), texcoord=Vec2()) -> None:
        self.position = position
        self.normal = normal
        self.color = color
        self.texcoord = texcoord
        

class MeshComponent(BaseComponents):
    _vertices: List[Vertex]
    _indices: np.ndarray
    _primitive_type: Constant
    

    def __init__(self, vertices:List[Vertex], indices:List[int], primitive_type = GL_TRIANGLES) -> None:
        super().__init__()
        self._vertices = vertices
        self._indices = np.array(indices, np.int32)
        self._primitive_type = primitive_type
        
        self._position_buffer = glGenBuffers(1)
        self._color_buffer = glGenBuffers(1)
        self._normal_buffer = glGenBuffers(1)
        self._indices_buffer = glGenBuffers(1)
        self._vbo_id = glGenVertexArrays(1)
        glBindVertexArray(self._vbo_id)
    
    def draw(self, program) -> None:
        glUseProgram(program)
        
        position_data = np.array([vertex.position._data for vertex in self._vertices], np.float32).flatten()
        glBindBuffer(GL_ARRAY_BUFFER, self._position_buffer)
        glBufferData(GL_ARRAY_BUFFER, position_data.nbytes, position_data, GL_STATIC_DRAW)
        
        indices_data = self._indices.flatten()
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self._indices_buffer)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices_data.nbytes, indices_data, GL_STATIC_DRAW)
        
        position = glGetAttribLocation(program, 'position')
        glEnableVertexAttribArray(position)
        glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 4, ctypes.c_void_p(0))
        
        glDrawElements(self._primitive_type, len(indices_data), GL_UNSIGNED_INT, None)
        
        # glBegin(self._primitive_type)
        # for edge in self._edges:
        #     for vertex in edge:
        #         glVertex3fv(self._vertices[vertex])
        # glEnd()