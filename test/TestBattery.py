import unittest
from datetime import date
from battery import SpindlerBattery, NubbinBattery

class TestBattery(unittest.TestCase):
    def test_spindler_battery_needs_service(self):
        # Test SpindlerBattery needs service
        last_service_date = date(2020, 1, 1)
        current_date = date(2023, 1, 1)
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_nubbin_battery_needs_service(self):
        # Test NubbinBattery needs service
        last_service_date = date(2018, 1, 1)
        current_date = date(2023, 1, 1)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

if __name__ == '__main__':
    unittest.main()