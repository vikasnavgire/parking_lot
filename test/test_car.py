import unittest

from logic.car import Car


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car_obj = Car()

    def test_reg_no(self):
        self.car_obj.reg_no = "1234"
        self.assertEqual(self.car_obj.reg_no, "1234")

    def test_colour(self):
        self.car_obj.colour = "red"
        self.assertEqual(self.car_obj.colour, "red")


if __name__ == '__main__':
    unittest.main()
