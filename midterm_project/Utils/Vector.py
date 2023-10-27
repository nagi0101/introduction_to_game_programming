from typing import Union

class Vec3:
    x:float=0
    y:float=0
    z:float=0
    
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    @classmethod
    def from_scalar(cls, scalar:float) -> "Vec3":
        return Vec3(scalar, scalar, scalar)
    
    def __neg__(self) -> "Vec3":
        return Vec3(-self.x, -self.y, -self.z)
    
    def __add__(self, other:"Vec3") -> "Vec3":
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __mul__(self, other:Union[int|float, "Vec3"]) -> "Vec3":        
        if(type(other)==int or type(other)==float):
            return Vec3(self.x * other, self.y * other, self.z * other)
        elif(type(other)==Vec3):
            return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
        
        assert(False)