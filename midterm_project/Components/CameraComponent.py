import numpy as np

from Components.BaseComponents import BaseComponents

from Utils.Transform import Transform

class CameraComponent(BaseComponents):
    def __init__(self, transform: Transform = Transform()) -> None:
        super().__init__(transform)
    
    def get_view_matrix(self) -> np.ndarray:
        owner_transform = self.owner_object.transform
        inv_rotation = (-owner_transform.rotate).rotation_matrix()
        # inv_rotation = owner_transform.rotation_matrix()
        inv_translate = (-owner_transform.translate).translate_matrix()
        # print(inv_translate)
        return np.matmul(inv_translate, inv_rotation)