from device1 import Device

class TemperatureSensor(Device):
    # Temperature sensor inherits from Device

    def __init__(self, deviceId, location, data):
        # type is fixed as "Temperature"
        super().__init__(deviceId, location, data, "Temperature")