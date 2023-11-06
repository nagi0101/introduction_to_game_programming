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
        return self.rotate.rotation_matrix()

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
        return np.matmul(np.matmul(scale, rotation), translate)

    def get_forward_vector(self) -> Vec3:
        return self.rotate.rotate_vec3(Vec3(0, 0, -1))