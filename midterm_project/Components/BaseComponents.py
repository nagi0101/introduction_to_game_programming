class BaseComponents:
    parent = None
    children = []
    owner_object = None
    
    def tick(self, deltatime):
        for child in self.children:
            child.tick(deltatime)
    

