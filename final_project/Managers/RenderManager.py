from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from Game import Game
    from Components.MeshComponent import MeshComponent
    from Components.LightComponent import LightComponent

import pygame
import OpenGL
if __debug__:
    OpenGL.ERROR_LOGGING = True
else:
    OpenGL.ERROR_LOGGING = False
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from Utils.Singleton import Singleton

class RenderManager(metaclass=Singleton):
    _game:"Game"
    _screen:pygame.Surface
    _mesh_components:List["MeshComponent"]=[]
    _light_components:List["LightComponent"]=[]
    
    # Shader source
    _vertex_shader_source = b"""
    #version 330
    uniform mat4 model;
    uniform mat4 view;
    uniform mat4 proj;
    
    layout(location = 0) in vec3 position;
    layout(location = 1) in vec3 color;
    layout(location = 2) in vec3 normal;
    in vec2 texCoords;
    
    out vec4 vColorOut;
    out vec2 vTexCoordOut;
    out vec3 vNormalOut;
    out vec3 vPosWorld;
    
    void main()
    {
        vPosWorld = (model * vec4(position, 1.0)).rgb;
        gl_Position = proj * view * model * vec4(position, 1.0);
        vColorOut = vec4(color, 1.0);
        vTexCoordOut = texCoords;
        vNormalOut = (model * vec4(normal, 0.0)).rgb;
    }
    """
    _fragment_shader_source = b"""
    #version 330
    
    #define MAX_LIGHTS 2
    
    struct Light
    {
        vec3 strength;
        float fallOffStart;
        float fallOffEnd;
        vec3 direction;
        vec3 position;
    };
    
    struct Material
    {
        vec3 ambient;
        vec3 diffuse;
        vec3 specular;
        float shininess;
    };
    
    in vec4 vColorOut;
    in vec2 vTexCoordOut;
    in vec3 vNormalOut;
    in vec3 vPosWorld;
    
    uniform Light lights[MAX_LIGHTS];
    uniform sampler2D sampler;
    uniform Material material;
    uniform bool useTexture;
    uniform vec3 eyeWorld;
    
    out vec4 FragColor;
    
    float CalcAttenuation(float d, float falloffStart, float falloffEnd)
    {
        return clamp((falloffEnd - d) / (falloffEnd - falloffStart), 0.0, 1.0);
    }
    
    vec3 BlinnPhong(vec3 lightStrength, vec3 lightVec, vec3 normal,
                    vec3 toEye, Material mat)
    {
        vec3 toLight = -lightVec;
        float diff = max(dot(normal, toLight), 0.0);
        
        vec3 h = normalize(toLight + toEye);
        float ndoth = dot(normal, h);
        float spec = pow(max(ndoth, 0.0), mat.shininess);
        
        return lightStrength * (mat.ambient + mat.diffuse * diff + mat.specular * spec);
    }

    vec3 ComputeDirectionalLight(Light L, Material mat, vec3 normal,
                                    vec3 toEye)
    {
        return BlinnPhong(L.strength, L.direction, normal, toEye, mat);
    }
    
    vec3 ComputePointLight(Light L, Material mat, vec3 pos, vec3 normal,
                            vec3 toEye)
    {
        vec3 lightVec = pos - L.position;

        float d = length(lightVec);

        if (d > L.fallOffEnd)
        {
            return vec3(0.0, 0.0, 0.0);
        }
        else
        {
            lightVec /= d;
            float att = CalcAttenuation(d, L.fallOffStart, L.fallOffEnd);
            return BlinnPhong(att * L.strength, lightVec, normal, toEye, mat);
        }
    }
    
    vec3 ComputeSpotLight(Light L, Material mat, vec3 pos, vec3 normal,
                         vec3 toEye)
    {
        vec3 lightVec = pos - L.position;

        float d = length(lightVec);

        if (d > L.fallOffEnd)
        {
            return vec3(0.0f, 0.0f, 0.0f);
        }
        else
        {
            lightVec /= d;
            float att = CalcAttenuation(d, L.fallOffStart, L.fallOffEnd);
            float spot = dot(lightVec, L.direction);
            return BlinnPhong(att * spot * L.strength, lightVec, normal, toEye, mat);
        }
    }
    
    void main()
    {
        vec3 toEye = normalize(eyeWorld - vPosWorld);
        vec3 color = vec3(0.0, 0.0, 0.0);
        
        for(int i = 0; i < MAX_LIGHTS; ++i)
        {
            //color += ComputeDirectionalLight(lights[i], material, vNormalOut, toEye);
            //color += ComputePointLight(lights[i], material, vPosWorld, vNormalOut, toEye);
            color += ComputeSpotLight(lights[i], material, vPosWorld, vNormalOut, toEye);
        }
        
        vec4 texColor = texture(sampler, vTexCoordOut);
        FragColor = texColor * vec4(color, 1.0);
    }
    """
    def __init__(self, game) -> None:
        self._game = game
        self._screen = pygame.display.set_mode((720, 480), pygame.DOUBLEBUF|pygame.OPENGL)
        display = self._screen.get_size()
        gluPerspective(45, (display[0]/display[1]), 0.001, 1000.0)
        
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
        
    def append_light(self, light_component):
        self._light_components.append(light_component)
    
    def remove_light(self, light_component):
        self._light_components.remove(light_component)
    
    def draw(self) -> None:
        glUseProgram(self._shader_program)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        location = glGetUniformLocation(self._shader_program, 'eyeWorld')
        glUniform3fv(location, 1, self._game.player.transform.translate._data)

        for idx, lightComponent in enumerate(self._light_components):
            lightComponent.copy_data_to_index(self._shader_program, idx)

        view_loc = glGetUniformLocation(self._shader_program, 'view')
        view_matrix = self._game.player.camera.get_view_matrix()
        glUniformMatrix4fv(view_loc, 1, GL_FALSE, view_matrix)
        
        proj_loc = glGetUniformLocation(self._shader_program, 'proj')
        proj_matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
        glUniformMatrix4fv(proj_loc, 1, GL_FALSE, proj_matrix)

        for mesh_comp in self._mesh_components:
            mesh_comp.draw(self._shader_program)
        
        pygame.display.flip()

    @property
    def screen(self) -> None:
        return self._screen
    @screen.setter
    def screen(self, screen:pygame.Surface):
        self._screen = screen

    