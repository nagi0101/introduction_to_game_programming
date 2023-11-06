from GameObjects.GameObject import GameObject
from Utils.Transform import Transform

from Managers.MeshManager import MeshManager

class CollidableBox(GameObject):
    def __init__(self, transform:Transform=Transform()) -> None:
        super().__init__(transform)
        MeshManager.Factory.box(transform=transform)
    
    def update(self, deltatime):
        dv = self.game.player.transform.translate - self.transform.translate
        print(dv._data)
        
        super().update(deltatime)
        