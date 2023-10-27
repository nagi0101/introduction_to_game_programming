
from Utils.Vector import Vec3
from Utils.Rotator import Rot3 

class Transform:
    translate = Vec3()
    rotate = Rot3()
    scale = Vec3()

class GameObject:
    components = []
    game = None
    transform = Transform()

    def add_component(self, component):
        self.components.append(component)
        component.owner_object = self

    def tick(self, deltatime):
        for component in self.components:
            component.tick(deltatime)