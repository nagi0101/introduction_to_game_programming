from GameObjects.GameObject import GameObject

from Components.MovementComponent import MovementComponent
from Components.CameraComponent import CameraComponent

from Managers.MeshManager import MeshManager 

from Utils.Vector import Vec3
from Utils.Transform import Transform

class Player(GameObject):
    def __init__(self, transform:Transform=Transform()) -> None:
        super().__init__(transform)
        self.camera = CameraComponent(transform=Transform(
            translate=Vec3(0, 0, 0.01)
        ))
        self.add_component(self.camera)
        # plane = MeshManager.Factory.plane(transform=Transform(
        #     translate=Vec3(0, 0, -0.5),
        #     scale=Vec3.from_scalar(0.01)
        # ), texture_path=".\\Resources\\Textures\\blocks1.jpg")
        self.add_component(plane)
        self.add_component(MovementComponent(speed=2.0))

    def update(self, deltatime):
        super().update(deltatime)