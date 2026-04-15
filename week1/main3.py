from smart_light3 import SmartLight
from smart_thermostat3 import SmartThermostat
from smart_lock3 import SmartLock

# Calls operate() on every device (polymorphism)
def operate_all(devices):
    print("\n--- Operating Devices ---")
    for d in devices:
        print(d.operate())
    print("--- Done ---\n")

def main():
    devices = []  # List to store created devices

    while True:
        print("Menu:")
        print("1 - Add Smart Device")
        print("2 - Operate Devices")
        print("0 - Exit")

        choice = input("Your choice: ")

        # Add a new device
        if choice == "1":
            print("1 - Smart Light")
            print("2 - Smart Thermostat")
            print("3 - Smart Lock")

            t = input("Type: ")
            name = input("Device Name: ")
            status = input("Status (on/off): ")

            # Create Smart Light
            if t == "1":
                brightness = input("Brightness (1-100): ")
                devices.append(SmartLight(name, status, brightness))

            # Create Smart Thermostat
            elif t == "2":
                temp = input("Temperature: ")
                devices.append(SmartThermostat(name, status, temp))

            # Create Smart Lock
            elif t == "3":
                locked = input("Locked? (yes/no): ")
                devices.append(SmartLock(name, status, locked == "yes"))

            else:
                print("Invalid type.")

        # Operate all devices
        elif choice == "2":
            if len(devices) == 0:
                print("No devices added.")
            else:
                operate_all(devices)

        # Exit program
        elif choice == "0":
            print("Program ending.")
            break

        # Invalid menu choice
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()