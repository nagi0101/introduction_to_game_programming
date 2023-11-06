from typing import Union

import numpy as np

class Vec2:
    _data:np.ndarray
    
    def __init__(self, x=0, y=0):
        self._data = np.array((x, y), np.float32)
    
    @property
    def x(self) -> np.float32:
        return float(self._data[0])
    @x.setter
    def x(self, x:float):
        self._data[0] = x
    
    @property
    def y(self) -> np.float32:
        return float(self._data[1])
    @y.setter
    def y(self, y:float):
        self._data[1] = y
    
    @classmethod
    def from_scalar(cls, scalar:float) -> "Vec2":
        return Vec2(scalar, scalar)
    
    def __neg__(self) -> "Vec2":
        return Vec2(-self.x, -self.y)
    
    def __add__(self, other:"Vec2") -> "Vec2":
        return Vec2(self.x + other.x, self.y + other.y)
    
    def __mul__(self, other:Union[int|float, "Vec2"]) -> "Vec2":        
        if(type(other)==int or type(other)==float):
            return Vec2(self.x * other, self.y * other)
        elif(type(other)==Vec2):
            return Vec2(self.x * other.x, self.y * other.y)

class Vec3:
    def __init__(self, x:int|float=0, y:int|float=0, z:int|float=0):
        data = np.array((x, y, z), np.float32)
        self._data = np.array((x, y, z), np.float32)
    
    def translate_matrix(self) -> np.ndarray:
        x = self.x
        y = self.y
        z = self.z
        return np.array((
            (1, 0, 0, 0),
            (0, 1, 0, 0),
            (0, 0, 1, 0),
            (x, y, z, 1),
        ), np.float32)

    def scale_matrix(self) -> np.ndarray:
        x = self.x
        y = self.y
        z = self.z
        return np.array((
            (x, 0, 0, 0),
            (0, y, 0, 0),
            (0, 0, z, 0),
            (0, 0, 0, 1),
        ), np.float32)
    
    @property
    def x(self) -> float:
        return float(self._data[0])
    @x.setter
    def x(self, x:float):
        self._data[0] = x
    
    @property
    def y(self) -> float:
        return float(self._data[1])
    @y.setter
    def y(self, y:float):
        self._data[1] = y

    @property
    def z(self) -> float:
        return float(self._data[2])
    @z.setter
    def z(self, z:float):
        self._data[2] = z

    @property
    def norm(self)->float:
        return np.linalg.norm(self._data)
    
    @classmethod
    def from_scalar(cls, scalar:float) -> "Vec3":
        return Vec3(scalar, scalar, scalar)
    
    def __neg__(self) -> "Vec3":
        return Vec3(-self.x, -self.y, -self.z)
    
    def __sub__(self, other) -> "Vec3":
        return self + (-other)
    
    def __add__(self, other:"Vec3") -> "Vec3":
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __mul__(self, other:Union[int|float, "Vec3"]) -> "Vec3":        
        if(type(other)==int or type(other)==float):
            return self * Vec3.from_scalar(other)
        elif(type(other)==Vec3):
            return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
