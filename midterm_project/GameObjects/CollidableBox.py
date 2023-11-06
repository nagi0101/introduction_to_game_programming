from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Components.MeshComponent import MeshComponent

from GameObjects.GameObject import GameObject
from Utils.Transform import Transform

from Managers.MeshManager import MeshManager

class CollidableBox(GameObject):
    mesh:"MeshComponent"
    threshold:float

    def __init__(self, transform:Transform=Transform(), threshold:float=0.0) -> None:
        super().__init__(transform)
        self.mesh = MeshManager.Factory.box(transform=transform)
        self.add_component(self.mesh)
        self.threshold = threshold
    
    def update(self, deltatime):
        dv = self.game.player.transform.translate - self.transform.translate
        if dv.norm <= self.threshold:
            self.on_collide()
        
        super().update(deltatime)
    
    def on_collide(self):
        print("Collide")
        self.game.remove_game_object(self)
