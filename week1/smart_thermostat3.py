from smart_device3 import SmartDevice

# Smart Thermostat device
class SmartThermostat(SmartDevice):
    def __init__(self, deviceName, status, temperature):
        # Call base class constructor
        super().__init__(deviceName, status)
        self.temperature = temperature

    def operate(self):
        # Thermostat-specific operation
        return f"{self.deviceName} thermostat set to {self.temperature}°C and is {self.status}."