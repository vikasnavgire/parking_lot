import unittest

from logic.lot import Lot
from logic.car import Car

class TestLot(unittest.TestCase):
    def setUp(self):
        self.lot_obj = Lot(1, available=True)
        self.car_obj = Car()
        self.car_obj.colour = "blue"
        self.car_obj.reg_no = "1234"

    def test_car(self):
        self.lot_obj.car = self.car_obj
        self.assertEqual(self.lot_obj.car.colour, "blue")

    def test_slot_no(self):
        self.assertEqual(self.lot_obj.slot_no, 1)

    def test_available(self):
        self.assertEqual(self.lot_obj.available, True)


if __name__ == '__main__':
    unittest.main()
