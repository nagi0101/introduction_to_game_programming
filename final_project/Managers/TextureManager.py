from typing import Dict

import OpenGL
if __debug__:
    OpenGL.ERROR_LOGGING = True
else:
    OpenGL.ERROR_LOGGING = False
from OpenGL.GL import *
import numpy as np
from PIL import Image

from Utils.Singleton import Singleton


class Texture:
    def __init__(self, filename) -> None:
        self._texture_buffer_id = glGenTextures(1)
        img = Image.open(filename)
        img_data = np.array(list(img.getdata()), np.int8)
        
        glBindTexture(GL_TEXTURE_2D, self._texture_buffer_id)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)

    @property
    def buffer_id(self):
        return self._texture_buffer_id


class TextureManager(metaclass=Singleton):
    textures:Dict[str, Texture]
    
    def __init__(self) -> None:
        self.textures = {}
    
    def add_texture(self, filename:str) -> Texture:
        texture = Texture(filename)
        self.textures[filename] = texture
        return self.textures[filename]
    
    def get_texture(self, filename:str) -> Texture:
        return self.textures[filename]

    def add_or_get(self, filename:str) -> Texture:
        if(filename in self.textures.keys()):
            return self.get_texture(filename)
        return self.add_texture(filename)