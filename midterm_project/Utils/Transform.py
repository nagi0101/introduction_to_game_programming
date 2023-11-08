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
        return self.translate.translate_matrix()

    def scale_matrix(self) -> np.ndarray:
        return self.scale.scale_matrix()

    def transform_matrix(self) -> np.ndarray:
        scale = self.scale_matrix()
        rotation = self.rotation_matrix()
        translate = self.translate_matrix()
        return np.matmul(np.matmul(scale, rotation), translate)

    def get_forward_vector(self) -> Vec3:
        return self.rotate.rotate_vec3(Vec3(0, 0, -1))
    

    def __add__(self, other:"Transform") -> "Transform":
        return Transform(
            translate=self.translate + other.translate, 
            rotate=self.rotate + other.rotate, 
            scale=self.scale + other.scale
            )
    
    def __mul__(self, other:int|float) -> "Transform":        
        if(type(other)==int or type(other)==float):
            return Transform(
                translate=self.translate * other,
                rotate=self.rotate * other,
                scale=self.scale * other
                )

    @classmethod
    def lerp(cls, a, b, alpha) -> "Transform":
        return a * (1 - alpha) + b * alpha