from Utils.Vector import Vec3
from Utils.Rotator import Rot3

class Transform:
    translate: Vec3
    rotate: Rot3
    scale: Vec3
    
    def __init__(self, translate:Vec3 = Vec3(), rotate:Rot3 = Rot3(), scale:Vec3 = Vec3()) -> None:
        self.translate = translate
        self.rotate = rotate
        self.scale = scale
        