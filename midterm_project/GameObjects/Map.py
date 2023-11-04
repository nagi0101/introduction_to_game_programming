from GameObjects.GameObject import GameObject

from Managers.MeshManager import MeshManager

_ = 0
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

class Map(GameObject):
    def __init__(self) -> None:
        super().__init__()
        for mesh_comp in MeshManager.Factory.from_map(map_data):
            self.add_component(mesh_comp)