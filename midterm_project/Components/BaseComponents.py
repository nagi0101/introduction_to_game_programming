class BaseComponents:
    childs = []
    owner_object = None
    tickable = False
    
    def tick(self, deltatime):
        for child in self.childs:
            if self.tickable:
                child.tick(deltatime)
    

