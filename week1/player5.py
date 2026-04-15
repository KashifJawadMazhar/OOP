from entity5 import Entity

# Player entity with player-specific interaction
class Player(Entity):
    def __init__(self, name, position, health):
        super().__init__(name, position)
        self.health = health

    def interact(self):
        return f"Player {self.name} interacts by exploring the world."