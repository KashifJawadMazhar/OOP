from smart_device3 import SmartDevice

# Smart Light device
class SmartLight(SmartDevice):
    def __init__(self, deviceName, status, brightness):
        # Call base class constructor
        super().__init__(deviceName, status)
        self.brightness = brightness

    def operate(self):
        # Light-specific operation
        return f"{self.deviceName} light is {self.status} at brightness {self.brightness}."