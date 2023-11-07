from typing import List

from GameObjects.GameObject import GameObject

from Utils.Transform import Transform
from Utils.Vector import Vec3

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
        ".\\Resources\\Textures\\wall01.jpg"
    ]
    
    def __init__(self, transform:Transform=Transform()) -> None:
        super().__init__(transform)
        for mesh_comp in MeshManager.Factory.from_map(self.map_data, self.textures):
            self.add_component(mesh_comp)

    def get_empty_pos(self)->List[Vec3]:
        empty_list = []
        for idx_z, z in enumerate(self.map_data):
            for idx_x, x in enumerate(z):
                if x == 0:
                    empty_list.append(Vec3(idx_x, 0, idx_z))
        return empty_list