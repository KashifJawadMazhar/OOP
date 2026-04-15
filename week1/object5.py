from entity5 import Entity

# Object entity with pickup/use interaction
class Object(Entity):
    def __init__(self, name, position, objType):
        super().__init__(name, position)
        self.objType = objType

    def interact(self):
        return f"Object {self.name} interacts by being used as a {self.objType}."