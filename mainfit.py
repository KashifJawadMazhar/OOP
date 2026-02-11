
from fitnesstracker import FitnessTracker

def main():
    print("Program starting.")
    print("Tervetuloa!")
    tracker = FitnessTracker()

    while True:
        print("\nOptions:")
        print("1) Add steps")
        print("2) Add calories burned")
        print("3) View daily summary")
        print("0) Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            try:
                steps = int(input("Enter the number of steps: "))
                tracker.addSteps(steps)
                print(f"{steps} steps added.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        elif choice == "2":
            try:
                calories = float(input("Enter the number of calories burned: "))
                tracker.addCalories(calories)
                print(f"{calories:.2f} calories added.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        elif choice == "3":
            print("Daily Summary:")
            print(tracker.getSummary())
        elif choice == "0":
            print("Kiitos Paljon!")
            print("Program ending.")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()