from enum import Enum

class MeasurementError(Exception):
    pass

class DeviceError(Exception):
    pass

class MODE(Enum):
    DCV = 1
    ACV = 2
    DCI = 3
    ACI = 4
    RES = 5

class Multimeter:
    def __init__(self, device):
        self.device = device
        self.mode_dictionary =             {
                MODE.DCV: "dc_v",
                MODE.ACV: "ac_v",
                MODE.DCI: "dc_i",
                MODE.ACI: "ac_i",
                MODE.RES: "res"
            }

    def setMode(self, mode):
         self.device.set_measurement_mode(self.mode_dictionary.get(mode))

    def setRange(self, range):
        self.device.set_measurement_range(range)

    def measure(self)-> float:
        try:
            return self.device.get_measurement_value()
        except DeviceError:
            raise MeasurementError('Can not perform measurement!')
