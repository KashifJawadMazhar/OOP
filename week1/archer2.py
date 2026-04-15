from game_character2 import GameCharacter

# Archer character with ranged abilities
class Archer(GameCharacter):

    def attack(self):
        return f"{self.name} shoots an arrow."

    def defend(self):
        return f"{self.name} dodges quickly."