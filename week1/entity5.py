# Base class for all VR simulation entities
class Entity:
    def __init__(self, name, position):
        # Common attributes for all entities
        self.name = name
        self.position = position

    def interact(self):
        # Will be overridden in subclasses
        pass