from GameObjects.GameObject import GameObject

from Utils.Transform import Transform

from Managers.MeshManager import MeshManager

_ = 0

class Map(GameObject):    
    map_data = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, _, _, _, _, _, _, 1, _, 1],
        [1, _, _, 1, _, _, _, 1, _, 1],
        [1, _, 1, 1, _, _, _, _, _, 1],
        [1, _, _, _, _, 1, _, _, _, 1],
        [1, _, _, 1, 1, 1, _, _, _, 1],
        [1, _, _, _, 1, _, _, _, _, 1],
        [1, _, _, _, 1, _, _, 1, _, 1],
        [1, _, _, _, _, _, _, _, _, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    textures = [
        ".\\Resources\\Textures\\blocks1.jpg"
    ]
    
    def __init__(self, transform:Transform=Transform()) -> None:
        super().__init__(transform)
        for mesh_comp in MeshManager.Factory.from_map(self.map_data, self.textures):
            self.add_component(mesh_comp)