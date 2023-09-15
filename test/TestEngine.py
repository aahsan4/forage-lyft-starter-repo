import unittest
from datetime import date
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine

class TestEngine(unittest.TestCase):
    def test_capulet_engine_needs_service(self):
        engine = CapuletEngine(last_service_mileage=25000, current_mileage=55000)
        self.assertTrue(engine.needs_service())

    def test_sternman_engine_needs_service(self):
        engine_with_warning = SternmanEngine(warning_light_on=True)
        engine_without_warning = SternmanEngine(warning_light_on=False)
        self.assertTrue(engine_with_warning.needs_service())
        self.assertFalse(engine_without_warning.needs_service())

    def test_willoughby_engine_needs_service(self):
        engine = WilloughbyEngine(last_service_mileage=40000, current_mileage=100000)
        self.assertTrue(engine.needs_service())

if __name__ == '__main__':
    unittest.main()