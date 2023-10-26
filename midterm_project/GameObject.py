class GameObject:
    components = []
    game=None

    def add_component(self, component):
        self.components.append(component)
        component.owner_object = self

    def tick(self):
        for component in self.components:
            component.tick()