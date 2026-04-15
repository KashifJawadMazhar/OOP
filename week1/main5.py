from player5 import Player
from npc5 import NPC
from object5 import Object

# Calls interact() on every entity (polymorphism)
def interact_all(entities):
    print("\n--- Interactions ---")
    for e in entities:
        print(e.interact())
    print("--- End ---\n")

def main():
    entities = []  # List to store all created entities

    while True:
        print("Menu:")
        print("1 - Add Entity")
        print("2 - Interact with Entities")
        print("3 - Exit")

        choice = input("Your choice: ")

        # Add entity
        if choice == "1":
            print("1 - Player")
            print("2 - NPC")
            print("3 - Object")

            t = input("Type: ")
            name = input("Name: ")
            position = input("Position: ")

            if t == "1":
                health = input("Health: ")
                entities.append(Player(name, position, health))

            elif t == "2":
                role = input("Role: ")
                entities.append(NPC(name, position, role))

            elif t == "3":
                objType = input("Object Type: ")
                entities.append(Object(name, position, objType))

            else:
                print("Invalid type.")

        # Interact with all entities
        elif choice == "2":
            if len(entities) == 0:
                print("No entities added.")
            else:
                interact_all(entities)

        # Exit
        elif choice == "3":
            print("Program ending.")
            break

        # Invalid menu choice
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()