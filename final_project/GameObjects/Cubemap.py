from GameObjects.GameObject import GameObject

from Managers.MeshManager import MeshManager

from Utils.Transform import Transform

class Cubemap(GameObject):
    def __init__(self, transform: Transform = Transform()) -> None:
        super().__init__(transform)
        
        meshes = MeshManager.Factory.cubemap(100, (
            "final_project\\Resources\\Textures\\skybox\\front.jpg",
            "final_project\\Resources\\Textures\\skybox\\back.jpg",
            "final_project\\Resources\\Textures\\skybox\\right.jpg",
            "final_project\\Resources\\Textures\\skybox\\left.jpg",
            "final_project\\Resources\\Textures\\skybox\\top.jpg",
            "final_project\\Resources\\Textures\\skybox\\bottom.jpg",
        ))
        
        for meshComp in meshes:
            self.add_component(meshComp)

        