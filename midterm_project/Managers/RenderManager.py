import pygame
import OpenGL
if __debug__:
    OpenGL.ERROR_LOGGING = True
else:
    OpenGL.ERROR_LOGGING = False
from OpenGL.GL import *
from OpenGL.GLU import *

import numpy as np

from Utils.Singleton import Singleton

from Managers.TimeManager import TimeManager
from Managers.MeshManager import MeshManager

class RenderManager(metaclass=Singleton):
    _game=None
    _screen:pygame.Surface
    
    # Shader source
    _vertex_shader_source = b"""
    #version 130
    uniform mat4 view;
    in vec3 position;
    void main()
    {
        gl_Position = view * vec4(position, 1.0);
    }
    """
    _fragment_shader_source = b"""
    #version 130
    out vec4 FragColor;
    void main()
    {
        FragColor = vec4(1.0f, 1.0f, 1.0f, 1.0f);
    }
    """
    def __init__(self, game) -> None:
        self._game = game
        display = (800, 600)
        self._screen = pygame.display.set_mode(display, pygame.DOUBLEBUF|pygame.OPENGL)
        gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)
        
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

    def draw(self) -> None:
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glRotatef(1 * TimeManager().delta_second, 3, 1, 1)
        view_loc = glGetUniformLocation(self._shader_program, 'view')
        view_matrix = glGetFloatv(GL_PROJECTION_MATRIX).T
        glUniformMatrix4fv(view_loc, 1, GL_FALSE, view_matrix)
        
        cube = MeshManager.Factory.line_box(0.1)
        cube.draw(self._shader_program)
        pygame.display.flip()

    @property
    def screen(self) -> None:
        return self.screen
    @screen.setter
    def screen(self, screen:pygame.Surface):
        self._screen = screen

    