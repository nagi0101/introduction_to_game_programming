from math import pi

import pygame
import OpenGL
if __debug__:
    OpenGL.ERROR_LOGGING = True
else:
    OpenGL.ERROR_LOGGING = False
from OpenGL.GL import *
from OpenGL.GLU import *

from Utils.Singleton import Singleton

from Managers.TimeManager import TimeManager

class RenderManager(metaclass=Singleton):
    _game=None
    _screen:pygame.Surface
    _mesh_components=[]
    
    # Shader source
    _vertex_shader_source = b"""
    #version 330
    uniform mat4 view;
    uniform mat4 proj;
    
    layout(location = 0) in vec3 position;
    layout(location = 1) in vec3 color;
    
    out vec4 vColorOut;
    
    void main()
    {
        gl_Position = proj * view * vec4(position, 1.0);
        vColorOut = vec4(color, 1.0);
    }
    """
    _fragment_shader_source = b"""
    #version 330
    in vec4 vColorOut;
    
    out vec4 FragColor;
    
    void main()
    {
        FragColor = vColorOut;
    }
    """
    def __init__(self, game) -> None:
        self._game = game
        display = (800, 600)
        self._screen = pygame.display.set_mode(display, pygame.DOUBLEBUF|pygame.OPENGL)
        gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5.0)
        
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
        glDepthMask(GL_TRUE)
        
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    def append_mesh(self, mesh_component):
        self._mesh_components.append(mesh_component)
    
    def draw(self) -> None:
        glUseProgram(self._shader_program)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        glRotatef(pi * TimeManager().delta_second, 0, 1, 0)
        
        view_loc = glGetUniformLocation(self._shader_program, 'view')
        view_matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
        glUniformMatrix4fv(view_loc, 1, GL_FALSE, view_matrix)
        
        proj_loc = glGetUniformLocation(self._shader_program, 'proj')
        proj_matrix = glGetFloatv(GL_PROJECTION_MATRIX)
        glUniformMatrix4fv(proj_loc, 1, GL_FALSE, proj_matrix)

        for mesh_comp in self._mesh_components:
            mesh_comp.draw(self._shader_program)
        
        pygame.display.flip()

    @property
    def screen(self) -> None:
        return self.screen
    @screen.setter
    def screen(self, screen:pygame.Surface):
        self._screen = screen

    