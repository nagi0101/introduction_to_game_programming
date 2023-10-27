from typing import List

from GameObject import GameObject

class BaseComponents:
    parent:"BaseComponents" = None
    children:List["BaseComponents"] = []
    owner_object:GameObject = None
    
    def tick(self, deltatime):
        for child in self.children:
            child.tick(deltatime)
    
    def append_child(self, child:"BaseComponents"):
        child.parent = self
        child.owner_object = self.owner_object
        self.children.append(child)

