from GameObjects.GameObject import GameObject

from Components.MovementComponent import MovementComponent
from Managers.MeshManager import MeshManager


class Player(GameObject):
    def __init__(self) -> None:
        super().__init__()
        self.add_component(MovementComponent(speed=5.0))
        self.add_component(MeshManager().Factory.box())
        
    def update(self, deltatime):
        super().update(deltatime)