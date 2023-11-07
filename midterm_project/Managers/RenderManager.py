from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from Game import Game
    from Components.MeshComponent import MeshComponent

import pygame
import OpenGL
if __debug__:
    OpenGL.ERROR_LOGGING = True
else:
    OpenGL.ERROR_LOGGING = False
from OpenGL.GL import *
from OpenGL.GLU import *

from Utils.Singleton import Singleton

class RenderManager(metaclass=Singleton):
    _game:"Game"
    _screen:pygame.Surface
    _mesh_components:List["MeshComponent"]=[]
    
    # Shader source
    _vertex_shader_source = b"""
    #version 330
    uniform mat4 model;
    uniform mat4 view;
    uniform mat4 proj;
    
    layout(location = 0) in vec3 position;
    layout(location = 1) in vec3 color;
    in vec2 texCoords;
    
    out vec4 vColorOut;
    out vec2 vTexCoordOut;
    
    void main()
    {
        gl_Position = proj * view * model * vec4(position, 1.0);
        vColorOut = vec4(color, 1.0);
        vTexCoordOut = texCoords;
    }
    """
    _fragment_shader_source = b"""
    #version 330
    in vec4 vColorOut;
    in vec2 vTexCoordOut;
    
    uniform sampler2D sampler;
    
    out vec4 FragColor;
    
    void main()
    {
        vec4 texColor = texture(sampler, vTexCoordOut);
        float z = clamp(1 - pow(gl_FragCoord.z, 2000), 0.0, 1.0);
        FragColor = texColor*z;
    }
    """
    def __init__(self, game) -> None:
        self._game = game
        display = (800, 600)
        self._screen = pygame.display.set_mode(display, pygame.DOUBLEBUF|pygame.OPENGL)
        gluPerspective(45, (display[0]/display[1]), 0.001, 50.0)
        
        vertex_shader = glCreateShader(GL_VERTEX_SHADER)
        glShaderSource(vertex_shader, self._vertex_shader_source)
        glCompileShader(vertex_shader)

        fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)
        glShaderSource(fragment_shader, self._fragment_shader_source)
        glCompileShader(fragment_shader)

        self._shader_program = glCreateProgram()
        glAttachShader(self._shader_program, vertex_shader)
        glAttachShader(self._shader_program, fragment_shader)
        glLinkProgram(self._shader_program)
        
        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)
        glDepthMask(GL_TRUE)
        
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    def append_mesh(self, mesh_component):
        self._mesh_components.append(mesh_component)
    
    def remove_mesh(self, mesh_component):
        self._mesh_components.remove(mesh_component)
    
    def draw(self) -> None:
        glUseProgram(self._shader_program)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        view_loc = glGetUniformLocation(self._shader_program, 'view')
        view_matrix = self._game.player.camera.get_view_matrix()
        glUniformMatrix4fv(view_loc, 1, GL_FALSE, view_matrix)
        
        proj_loc = glGetUniformLocation(self._shader_program, 'proj')
        proj_matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
        glUniformMatrix4fv(proj_loc, 1, GL_FALSE, proj_matrix)

        for mesh_comp in self._mesh_components:
            mesh_comp.draw(self._shader_program)
        
        pygame.display.flip()
    
    def draw_text(self, x, y, text):
        font = pygame.font.SysFont('arial', 64)                                     
        textSurface = font.render(text, True, (255, 255, 66, 255), (0, 0, 0, 255))
        textData = pygame.image.tostring(textSurface, "RGBA", True)
        glWindowPos2d(x, y)
        glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)
        
    def draw_gameover(self, clear_time:float) -> None:
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        self._screen.fill((0, 0, 0))
        self.draw_text(0, 0, "Clear time: " + str(int(clear_time)))
        pygame.display.flip()

        @property
        def screen(self) -> None:
            return self._screen
        @screen.setter
        def screen(self, screen:pygame.Surface):
            self._screen = screen

    