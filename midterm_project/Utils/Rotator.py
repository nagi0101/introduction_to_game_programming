from typing import Union
from math import cos, sin

import numpy as np

from Utils.Vector import Vec3

class Rot3:
    roll:float
    pitch:float
    yaw:float

    def __init__(self, roll:float=0, pitch:float=0, yaw:float=0):
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw
    
    def rotation_matrix(self) -> np.ndarray:
        roll = self.roll
        pitch = self.pitch
        yaw = self.yaw
        pitch_matrix = np.array((
            (1,         0,          0, 0),
            (0, cos(pitch), -sin(pitch), 0),
            (0, sin(pitch),  cos(pitch), 0),
            (0,         0,          0, 1)
        ), np.float32)
        yaw_matrix = np.array((
            ( cos(yaw), 0, sin(yaw), 0),
            (          0, 1,          0, 0),
            (-sin(yaw), 0, cos(yaw), 0),
            (          0, 0,          0, 1)
        ), np.float32)
        roll_matrix = np.array((
            (cos(roll), -sin(roll), 0, 0),
            (sin(roll),  cos(roll), 0, 0),
            (       0,         0, 1, 0),
            (       0,         0, 0, 1)
        ), np.float32)

        return np.transpose(np.matmul(yaw_matrix, np.matmul(pitch_matrix, roll_matrix)))

    def rotate_vec3(self, vec3:Vec3) -> Vec3:
        vec4 = np.append(vec3._data, 0)
        rotated = np.matmul(vec4, self.rotation_matrix())
        return Vec3(rotated[0], rotated[1], rotated[2])
    
    @classmethod
    def from_scalar(cls, scalar:float) -> "Rot3":
        return Rot3(scalar, scalar, scalar)
    
    def __neg__(self) -> "Rot3":
        return Rot3(-self.roll, -self.pitch, -self.yaw)
    
    def __add__(self, other:"Rot3") -> "Rot3":
        return Rot3(self.roll + other.roll, self.pitch + other.pitch, self.yaw + other.yaw)
    
    def __mul__(self, other:Union[int|float, "Rot3"]) -> "Rot3":        
        if(type(other)==int or type(other)==float):
            return self * Rot3.from_scalar(other)
        elif(type(other)==Rot3):
            return Rot3(self.roll * other.roll, self.pitch * other.pitch, self.yaw * other.yaw)