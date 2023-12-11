from GameObjects.GameObject import GameObject

from Managers.MeshManager import MeshManager

from Utils.Transform import Transform

class Cubemap(GameObject):
    def __init__(self, transform: Transform = Transform()) -> None:
        super().__init__(transform)
        
        meshes = MeshManager.Factory.cubemap(100, (
            "Resources/Textures/skybox/front.jpg",
            "Resources/Textures/skybox/back.jpg",
            "Resources/Textures/skybox/right.jpg",
            "Resources/Textures/skybox/left.jpg",
            "Resources/Textures/skybox/top.jpg",
            "Resources/Textures/skybox/bottom.jpg",
        ))
        
        for meshComp in meshes:
            self.add_component(meshComp)

        