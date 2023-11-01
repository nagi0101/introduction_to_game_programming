from GameObject import GameObject

from Components.MovementComponent import MovementComponent
from Managers.MeshManager import MeshManager


class Player(GameObject):
    def __init__(self):
        self.add_component(MovementComponent(speed=5.0))
        self.add_component(MeshManager().Factory.box())
        
    def tick(self, deltatime):
        super().tick(deltatime)