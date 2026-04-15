from game_character2 import GameCharacter

# Warrior character with its own attack and defend style
class Warrior(GameCharacter):

    def attack(self):
        return f"{self.name} attacks with a sword."

    def defend(self):
        return f"{self.name} blocks with a shield."