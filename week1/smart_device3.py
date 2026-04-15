class SmartDevice:
    # Base class for all smart devices
    def __init__(self, deviceName, status):
        self.deviceName = deviceName
        self.status = status

    def operate(self):
        pass  # Overridden in subclasses