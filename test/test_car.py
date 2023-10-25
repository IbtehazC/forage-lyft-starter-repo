import unittest
from datetime import date
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service(self):
        current_date = date(2025, 5, 5)
        last_service_date = date(2020, 5, 5)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_no_need_for_service(self):
        current_date = date(2024, 5, 4)
        last_service_date = date(2020, 5, 5)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service(self):
        current_date = date(2022, 5, 5)
        last_service_date = date(2019, 5, 5)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_no_need_for_service(self):
        current_date = date(2021, 5, 4)
        last_service_date = date(2019, 5, 5)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service(self):
        engine = CapuletEngine(60000, 29000)
        self.assertTrue(engine.needs_service())

    def test_no_need_for_service(self):
        engine = CapuletEngine(30000, 10000)
        self.assertFalse(engine.needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_with_warning_light_on(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())

    def test_no_need_for_service_with_warning_light_off(self):
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service(self):
        engine = WilloughbyEngine(100000, 39000)
        self.assertTrue(engine.needs_service())

    def test_no_need_for_service(self):
        engine = WilloughbyEngine(50000, 10000)
        self.assertFalse(engine.needs_service())


if __name__ == '__main__':
    unittest.main()