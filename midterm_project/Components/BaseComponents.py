from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from GameObjects.GameObject import GameObject

class BaseComponents:
    parent:"BaseComponents" = None
    children:List["BaseComponents"] = []
    owner_object:"GameObject" = None
    
    def update(self, deltatime):
        for child in self.children:
            child.update(deltatime)
    
    def append_child(self, child:"BaseComponents"):
        child.parent = self
        child.owner_object = self.owner_object
        self.children.append(child)

