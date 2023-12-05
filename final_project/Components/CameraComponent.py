import numpy as np

from Components.BaseComponents import BaseComponents

from Utils.Transform import Transform

class CameraComponent(BaseComponents):
    def __init__(self, transform: Transform = Transform()) -> None:
        super().__init__(transform)
    
    def get_view_matrix(self) -> np.ndarray:
        transform = self.get_absolute_transform_matrix()
        return np.linalg.inv(transform)