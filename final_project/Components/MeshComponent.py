from typing import List

import OpenGL
if __debug__:
    OpenGL.ERROR_LOGGING = True
else:
    OpenGL.ERROR_LOGGING = False
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

from Components.BaseComponents import BaseComponents

from Managers.RenderManager import RenderManager
from Managers.TextureManager import TextureManager

from Utils.Vector import Vec3, Vec2
from Utils.Transform import Transform


class Material:
    ambient:Vec3
    diffuse:Vec3
    specular:Vec3
    shininess:float
    
    def __init__(self, ambient:Vec3=Vec3.from_scalar(0.1), diffuse:Vec3=Vec3.from_scalar(0.45), specular:Vec3=Vec3.from_scalar(0.45), shininess=100) -> None:
        self.ambient=ambient
        self.diffuse=diffuse
        self.specular=specular
        self.shininess=shininess

class Vertex:
    position:Vec3
    normal:Vec3
    color:Vec3
    texcoord:Vec2

    def __init__(self, position=Vec3(), normal=Vec3(), color=Vec3(1, 1, 1), texcoord=Vec2()) -> None:
        self.position = position
        self.normal = normal
        self.color = color
        self.texcoord = texcoord
        

class MeshComponent(BaseComponents):
    _vertices: List[Vertex]
    _indices: np.ndarray
    _primitive_type: Constant
    material:Material

    def __init__(self, transform:Transform=Transform(), 
                 vertices:List[Vertex] = [], indices:List[int] = [], 
                 primitive_type:Constant = GL_TRIANGLES, texture_path:str|None=None, 
                 material:Material=Material()) -> None:
        super().__init__(transform)
        self.transform = transform
        self._vertices = vertices
        self._indices = np.array(indices, np.uint32)
        self._primitive_type = primitive_type
        self._texture_path = texture_path
        
        self._position_buffer = glGenBuffers(1)
        self._color_buffer = glGenBuffers(1)
        self._normal_buffer = glGenBuffers(1)
        self._indices_buffer = glGenBuffers(1)
        self._texcoord_buffer = glGenBuffers(1)
        
        self.material = material
        
        RenderManager().append_mesh(self)
    
    def draw(self, program) -> None:
        model_loc = glGetUniformLocation(program, 'model')
        model_matrix = self.get_absolute_transform_matrix()
        glUniformMatrix4fv(model_loc, 1, GL_FALSE, model_matrix)
        
        if self._texture_path:
            glUniform1i(glGetUniformLocation(program, "useTexture"), GL_TRUE)
            
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
            glBindTexture(GL_TEXTURE_2D, TextureManager().add_or_get(self._texture_path).buffer_id)
            
            texcoord_np = np.array([vertex.texcoord._data for vertex in self._vertices], np.float32)
            texcoord_data = texcoord_np.flatten()
            glBindBuffer(GL_ARRAY_BUFFER, self._texcoord_buffer)
            glBufferData(GL_ARRAY_BUFFER, texcoord_data.nbytes, texcoord_data, GL_STATIC_DRAW)
            buffer_id = glGetAttribLocation(program, 'texCoords')
            glVertexAttribPointer(buffer_id, 2, GL_FLOAT, GL_FALSE, 0, None)
            glEnableVertexAttribArray(buffer_id)
        else:
            glUniform1i(glGetUniformLocation(program, "useTexture"), GL_FALSE)
        
        position_np = np.array([vertex.position._data for vertex in self._vertices], np.float32)
        position_data = position_np.flatten()
        glBindBuffer(GL_ARRAY_BUFFER, self._position_buffer)
        glBufferData(GL_ARRAY_BUFFER, position_data.nbytes, position_data, GL_STATIC_DRAW)
        position = glGetAttribLocation(program, 'position')
        glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(position)
                
        color_np = np.array([vertex.color._data for vertex in self._vertices], np.float32)
        color_data = color_np.flatten()
        glBindBuffer(GL_ARRAY_BUFFER, self._color_buffer)
        glBufferData(GL_ARRAY_BUFFER, color_data.nbytes, color_data, GL_STATIC_DRAW)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(1)

        normal_np = np.array([vertex.normal._data for vertex in self._vertices], np.float32)
        normal_data = normal_np.flatten()
        glBindBuffer(GL_ARRAY_BUFFER, self._normal_buffer)
        glBufferData(GL_ARRAY_BUFFER, normal_data.nbytes, normal_data, GL_STATIC_DRAW)
        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(2)
        
        location = glGetUniformLocation(program, f"material.ambient")
        glUniform3fv(location, 1, self.material.ambient._data)
        location = glGetUniformLocation(program, f"material.diffuse")
        glUniform3fv(location, 1, self.material.diffuse._data)
        location = glGetUniformLocation(program, f"material.specular")
        glUniform3fv(location, 1, self.material.specular._data)
        location = glGetUniformLocation(program, f"material.shininess")
        glUniform1f(location, self.material.shininess)
        
        indices_data = self._indices
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self._indices_buffer)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices_data.nbytes, indices_data, GL_STATIC_DRAW)
        
        glDrawElements(self._primitive_type, len(indices_data), GL_UNSIGNED_INT, None)

