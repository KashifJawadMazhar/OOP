from temperature_sensor1 import TemperatureSensor
from humidity_sensor1 import HumiditySensor
from motion_sensor1 import MotionSensor
from device1 import Device
from file_handler1 import FileHandler

SEPARATOR = ","  # used for CSV formatting


def serialize_device(device: Device) -> str:
    # Convert Device object into CSV row string
    return f"{device.deviceId}{SEPARATOR}{device.location}{SEPARATOR}{device.data}{SEPARATOR}{device.type}"


def deserialize_device(row: str) -> Device:
    # Convert CSV row string back into Device object
    parts = row.split(SEPARATOR)
    deviceId = parts[0]
    location = parts[1]
    data = float(parts[2])
    type = parts[3]
    # We return a base Device object here
    return Device(deviceId, location, data, type)


def display_device(device: Device) -> None:
    # Print device information in readable format
    print(f"{device.type} | ID: {device.deviceId} | Location: {device.location} | Data: {device.data}")


def main():
    # List to store device objects in memory
    devices: list[Device] = []

    # File handler for reading/writing CSV
    file = FileHandler("devices.csv")

    while True:
        print("\nMenu:")
        print("1 - Add IoT Device")
        print("2 - Serialize Data")
        print("3 - Deserialize Data")
        print("4 - Encrypt Data")
        print("5 - Decrypt Data")
        print("0 - Exit")

        choice = input("Your choice: ")

        # 1. Add new IoT device
        if choice == "1":
            print("1 - Temperature")
            print("2 - Humidity")
            print("3 - Motion")
            t = input("Select type: ")

            deviceId = input("Device ID: ")
            location = input("Location: ")
            try:
                data = float(input("Data value: "))
            except:
                print("Invalid data value.")
                continue

            if t == "1":
                devices.append(TemperatureSensor(deviceId, location, data))
            elif t == "2":
                devices.append(HumiditySensor(deviceId, location, data))
            elif t == "3":
                devices.append(MotionSensor(deviceId, location, data))
            else:
                print("Invalid device type.")

        # 2. Serialize objects → CSV
        elif choice == "2":
            rows = []
            for d in devices:
                rows.append(serialize_device(d))
            file.write(rows)
            print("Data serialized.")

        # 3. Deserialize CSV → objects
        elif choice == "3":
            rows = file.read()
            devices.clear()
            for row in rows:
                device = deserialize_device(row)
                devices.append(device)
            print("Data deserialized.")
            print("Current devices:")
            for d in devices:
                display_device(d)

        # 4. Encrypt file
        elif choice == "4":
            file.encrypt()
            print("Data encrypted.")

        # 5. Decrypt file
        elif choice == "5":
            file.decrypt()
            print("Data decrypted.")

        # 0. Exit
        elif choice == "0":
            print("Program ending.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()