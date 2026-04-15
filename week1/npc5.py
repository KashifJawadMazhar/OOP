from entity5 import Entity

# NPC (Non-Player Character) with dialogue interaction
class NPC(Entity):
    def __init__(self, name, position, role):
        super().__init__(name, position)
        self.role = role

    def interact(self):
        return f"NPC {self.name} interacts by talking as a {self.role}."