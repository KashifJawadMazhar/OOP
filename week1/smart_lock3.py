from smart_device3 import SmartDevice

# Smart Lock device
class SmartLock(SmartDevice):
    def __init__(self, deviceName, status, locked):
        # Call base class constructor
        super().__init__(deviceName, status)
        self.locked = locked

    def operate(self):
        # Lock-specific operation
        return f"{self.deviceName} lock is {'locked' if self.locked else 'unlocked'}."