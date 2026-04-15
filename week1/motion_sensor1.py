from device1 import Device

class MotionSensor(Device):
    # Motion sensor inherits from Device

    def __init__(self, deviceId, location, data):
        # type is fixed as "Motion"
        super().__init__(deviceId, location, data, "Motion")