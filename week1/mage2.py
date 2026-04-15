from game_character2 import GameCharacter

# Mage character with magic abilities
class Mage(GameCharacter):

    def attack(self):
        return f"{self.name} casts a fireball."

    def defend(self):
        return f"{self.name} uses a magic barrier."