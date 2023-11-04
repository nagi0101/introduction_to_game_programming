from math import cos, sin

import numpy as np

from Utils.Vector import Vec3
from Utils.Rotator import Rot3

class Transform:
    translate: Vec3
    rotate: Rot3
    scale: Vec3
    
    def __init__(self, translate:Vec3 = Vec3(), rotate:Rot3 = Rot3(), scale:Vec3 = Vec3.from_scalar(1)) -> None:
        self.translate = translate
        self.rotate = rotate
        self.scale = scale

    def rotation_matrix(self) -> np.ndarray:
        euler = self.rotate
        roll = euler.roll
        pitch = euler.pitch
        yaw = euler.yaw
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

    def translate_matrix(self) -> np.ndarray:
        translate = self.translate
        x = translate.x
        y = translate.y
        z = translate.z
        return np.array((
            (1, 0, 0, 0),
            (0, 1, 0, 0),
            (0, 0, 1, 0),
            (x, y, z, 1),
        ), np.float32)

    def scale_matrix(self) -> np.ndarray:
        scale = self.scale
        x = scale.x
        y = scale.y
        z = scale.z
        return np.array((
            (x, 0, 0, 0),
            (0, y, 0, 0),
            (0, 0, z, 0),
            (0, 0, 0, 1),
        ), np.float32)

    def transform_matrix(self) -> np.ndarray:
        scale = self.scale_matrix()
        rotation = self.rotation_matrix()
        translate = self.translate_matrix()
        return np.matmul(translate, np.matmul(rotation, scale))

        