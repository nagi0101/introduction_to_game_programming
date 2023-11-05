from typing import TYPE_CHECKING, List

import numpy as np

from Utils.Transform import Transform

if TYPE_CHECKING:
    from GameObjects.GameObject import GameObject

class BaseComponents:
    parent:"BaseComponents" = None
    children:List["BaseComponents"] = []
    owner_object:"GameObject" = None
    transform: Transform
    
    def __init__(self, transform:Transform=Transform()) -> None:
        self.transform = transform
    
    def update(self, deltatime):
        for child in self.children:
            child.update(deltatime)
    
    def append_child(self, child:"BaseComponents"):
        child.parent = self
        child.owner_object = self.owner_object
        self.children.append(child)
        
    def get_world_transform_matrix(self) -> np.ndarray:
        return self.parent.get_absolute_transform_matrix()
    
    def get_model_transform_matrix(self) -> np.ndarray:
        return self.transform.transform_matrix()

    def get_absolute_transform_matrix(self) -> np.ndarray:
        if self.parent == None:
            return np.matmul(self.transform.transform_matrix(), self.owner_object.transform.transform_matrix())
        return np.matmul(self.transform.transform_matrix(), self.parent.transform.transform_matrix())