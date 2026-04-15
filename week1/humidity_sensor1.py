from device1 import Device

class HumiditySensor(Device):
    # Humidity sensor inherits from Device

    def __init__(self, deviceId, location, data):
        # type is fixed as "Humidity"
        super().__init__(deviceId, location, data, "Humidity")