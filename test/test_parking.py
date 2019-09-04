import io
import sys
import unittest

from logic.parking import Parking


class TestParking(unittest.TestCase):
    def setUp(self):
        self.parking_obj = Parking()
        self.parking_obj2 = Parking()
        self.parking_obj2.create_parking_lot(2)
        self.parking_obj2.park("MH14GN5463", "blue")
        self.parking_obj2.park("MH14GN5463", "blue")
        self.capturedOutput = io.StringIO()  # capture stdout
        sys.stdout = self.capturedOutput

    def tearDown(self): pass

    def test_create_parking_lot(self):
        self.parking_obj.create_parking_lot(5)
        sys.stdout = sys.__stdout__
        self.capturedOutput.getvalue()
        self.assertEqual(self.capturedOutput.getvalue(), 'Created a parking lot with 5 slots\n')

    def test_create_parking_lot_already_created(self):
        self.parking_obj2.create_parking_lot(2)
        sys.stdout = sys.__stdout__
        self.capturedOutput.getvalue()
        self.assertEqual(self.capturedOutput.getvalue(),
                         'Parking Lot already created\n')

    def test_create_parking_lot_incorrect_int(self):
        self.parking_obj.create_parking_lot(-10)
        sys.stdout = sys.__stdout__
        self.capturedOutput.getvalue()
        self.assertEqual(self.capturedOutput.getvalue(),
                         'Number of slots provided is incorrect.\n')

    def test_create_parking_lot_incorrect_return(self):
        self.assertEqual(self.parking_obj.create_parking_lot(2), None)

    def test_get_nearest_available_slot(self):
        self.parking_obj2.leave(2)
        free_lot_obj = self.parking_obj2.get_nearest_available_slot()
        self.assertEqual(free_lot_obj.slot_no, 2)

    def test_park(self):
        self.parking_obj.create_parking_lot(3)
        self.parking_obj.park("MH14GN5463", "blue")
        sys.stdout = sys.__stdout__
        self.capturedOutput.getvalue()
        self.assertEqual(self.capturedOutput.getvalue(),
                         'Created a parking lot with 3 slots\nAllocated slot number: 1\n')

    def test_park_lot_full(self):
        self.parking_obj2.park("test", 'blue')
        sys.stdout = sys.__stdout__
        self.assertEqual(self.capturedOutput.getvalue(),
                         'Sorry, parking lot is full.\n')

    def test_leave(self):
        self.parking_obj2.leave(2)
        sys.stdout = sys.__stdout__
        self.assertEqual(self.capturedOutput.getvalue(),
                         'Slot number 2 is free\n')

    def test_leave_not_exists_slot(self):
        self.parking_obj2.leave(4)
        sys.stdout = sys.__stdout__
        self.assertEqual(self.capturedOutput.getvalue(),
                         'Sorry, slot number does not exist in the parking lot.\n')

    def test_leave_not_exists_car(self):
        self.parking_obj2.leave(2)
        self.parking_obj2.leave(2)
        sys.stdout = sys.__stdout__
        self.assertEqual(self.capturedOutput.getvalue(),
                         'Slot number 2 is free\nNo car is present at slot number 2\n')

    def test_status(self):
        self.parking_obj2.status()
        sys.stdout = sys.__stdout__
        self.assertEqual(self.capturedOutput.getvalue(),
                         'SlotNo \t RegistrationNo \t Colour\n1\tMH14GN5463\tblue\n2\tMH14GN5463\tblue\n')

    def test__pre_checks(self):
        self.parking_obj._pre_checks()
        sys.stdout = sys.__stdout__
        self.assertEqual(self.capturedOutput.getvalue(), 'Parking Lot not created\n')

    def test_registration_numbers_for_cars_with_colour(self):
        self.parking_obj2.registration_numbers_for_cars_with_colour('blue')
        sys.stdout = sys.__stdout__
        self.assertEqual(self.capturedOutput.getvalue(), 'MH14GN5463MH14GN546\n')

    def test_registration_numbers_for_cars_with_colour_not_found(self):
        self.parking_obj2.registration_numbers_for_cars_with_colour('blue1')
        sys.stdout = sys.__stdout__
        self.assertEqual(self.capturedOutput.getvalue(), 'Not found\n')

    def test_slot_numbers_for_cars_with_colour(self):
        self.parking_obj2.slot_numbers_for_cars_with_colour('blue')
        sys.stdout = sys.__stdout__
        self.assertEqual(self.capturedOutput.getvalue(), '1 2\n')

    def test_slot_number_for_registration_number(self):
        self.parking_obj2.slot_number_for_registration_number('MH14GN5463')
        sys.stdout = sys.__stdout__
        self.assertEqual(self.capturedOutput.getvalue(), '1\n')


if __name__ == '__main__':
    unittest.main()