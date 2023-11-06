from typing import TYPE_CHECKING, List

from Utils.Transform import Transform

if TYPE_CHECKING:
    from Components.BaseComponents import BaseComponents
    from Game import Game

class GameObject:
    components: List["BaseComponents"]
    transform: "Transform"
    game: "Game"

    def __init__(self, transform:Transform=Transform()) -> None:
        self.components = []
        self.game = None
        self.transform = transform

    def add_component(self, component):
        self.components.append(component)
        component.owner_object = self

    def update(self, deltatime):
        for component in self.components:
            component.update(deltatime)
    
    def fixed_update(self, deltatime):
        for component in self.components:
            component.fixed_update(deltatime)