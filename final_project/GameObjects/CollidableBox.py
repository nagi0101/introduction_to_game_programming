from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Components.MeshComponent import MeshComponent

from GameObjects.GameObject import GameObject

from Utils.Transform import Transform
from Utils.Vector import Vec3
from Utils.Rotator import Rot3

from Managers.MeshManager import MeshManager

class CollidableBox(GameObject):
    mesh:"MeshComponent"
    threshold:float

    def __init__(self, transform:Transform=Transform(), threshold:float=0.0, texture_path:str=None) -> None:
        super().__init__(transform)
        self.mesh = MeshManager.Factory.box(transform=Transform(
            scale=Vec3.from_scalar(0.2)
        ), texture_path=texture_path)
        self.add_component(self.mesh)
        self.threshold = threshold
    
    def update(self, deltatime):
        self.transform.rotate += Rot3(1, 1, 1) * deltatime
        
        super().update(deltatime)
