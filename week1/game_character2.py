from abc import ABC, abstractmethod

# Base class for all game characters
class GameCharacter(ABC):

    def __init__(self, name):
        # Every character has a name
        self.name = name

    @abstractmethod
    def attack(self):
        # Must be implemented in child classes
        pass

    @abstractmethod
    def defend(self):
        # Must be implemented in child classes
        pass