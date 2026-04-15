class Device:
    # Base class for all IoT devices

    def __init__(self, deviceId, location, data, type):
        # Common attributes shared by all devices
        self.deviceId = deviceId
        self.location = location
        self.data = data
        self.type = type