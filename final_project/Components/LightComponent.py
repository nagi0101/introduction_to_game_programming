import OpenGL
if __debug__:
    OpenGL.ERROR_LOGGING = True
else:
    OpenGL.ERROR_LOGGING = False
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from Managers.RenderManager import RenderManager

from Components.BaseComponents import BaseComponents

from Utils.Transform import Transform
from Utils.Vector import Vec3

class LightComponent(BaseComponents):
    strength:Vec3
    falloffStart:float
    falloffEnd:float
    
    def __init__(self, transform:Transform=Transform(), strength:Vec3=Vec3.from_scalar(1),
                 falloffStart:float=0.0, falloffEnd:float=1.0) -> None:
        super().__init__(transform)
        self.strength = strength
        self.falloffStart = falloffStart
        self.falloffEnd = falloffEnd
        
        RenderManager().append_light(self)
    
    def copy_data_to_index(self, program, index):
        location = glGetUniformLocation(program, f"lights[{index}].strength")
        glUniform3fv(location, 1, self.strength._data)

        location = glGetUniformLocation(program, f"lights[{index}].fallOffStart")
        glUniform1f(location, self.falloffStart)

        location = glGetUniformLocation(program, f"lights[{index}].fallOffEnd")
        glUniform1f(location, self.falloffEnd)

        location = glGetUniformLocation(program, f"lights[{index}].direction")
        glUniform3fv(location, 1, self.transform.get_forward_vector()._data)

        location = glGetUniformLocation(program, f"lights[{index}].position")
        glUniform3fv(location, 1, self.transform.translate._data)