import unittest
from unittest.mock import Mock

from multimeter import Multimeter,MODE,MeasurementError,DeviceError

class MultimeterTest(unittest.TestCase):
    def __init__(self, methodName):
        super().__init__(methodName)
        self.device = None
        self.multimeter = None


    def test_multimeter_set_mode(self):
        # Setup
        self.device = Mock()  # Mock() replaces Device
        self.multimeter = Multimeter(self.device)

        # Exercise
        self.multimeter.set_mode(MODE.DCV)

        # Verify
        self.device.set_measurement_mode.assert_called_with("dc_v")

    def test_multimeter_set_range(self):
        # Setup
        self.device = Mock()  # Mock() replaces Device
        self.multimeter = Multimeter(self.device)

        # Exercise
        self.multimeter.set_range(10)

        # Verify
        self.device.set_measurement_range.assert_called_with(10)

    def test_multimeter_measurement(self):
        # Setup
        self.device = Mock()  # Mock() replaces Device
        self.device.get_measurement_value.return_value = 5.0
        self.multimeter = Multimeter(self.device)

        # Exercise
        result = self.multimeter.measure()

        # Verify
        self.assertAlmostEqual(5.0, result, 1e-3)

    def test_multimeter_measurement_error(self):
        # Setup
        self.device = Mock()  # Mock() replaces Device
        self.device.get_measurement_value.side_effect = DeviceError('Hardware problem!')
        self.multimeter = Multimeter(self.device)

        # Exercise & Verify
        with self.assertRaises(MeasurementError):
            self.multimeter.measure()

if __name__ == '__main__':
    unittest.main()
