from warrior2 import Warrior
from mage2 import Mage
from archer2 import Archer

# Runs attack() and defend() for every character
def simulate_battle(characters):
    print("\n--- Battle Start ---")
    for c in characters:
        print(c.attack())
        print(c.defend())
    print("--- Battle End ---\n")

def main():
    characters = []  # List to store created characters

    while True:
        print("Menu:")
        print("1 - Create Character")
        print("2 - Simulate Battle")
        print("0 - Exit")

        choice = input("Your choice: ")

        # Create a new character
        if choice == "1":
            print("1 - Warrior")
            print("2 - Mage")
            print("3 - Archer")

            t = input("Type: ")
            name = input("Name: ")

            # Create correct character based on user choice
            if t == "1":
                characters.append(Warrior(name))
            elif t == "2":
                characters.append(Mage(name))
            elif t == "3":
                characters.append(Archer(name))
            else:
                print("Invalid type.")

        # Run battle simulation
        elif choice == "2":
            if len(characters) == 0:
                print("No characters created.")
            else:
                simulate_battle(characters)

        # Exit program
        elif choice == "0":
            print("Program ending.")
            break

        # Invalid menu choice
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()