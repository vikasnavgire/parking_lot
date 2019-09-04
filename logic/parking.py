import logic.car as car
import logic.lot as lot


class Parking(object):
    """
    Parking class to handle parking operations
    """

    def __init__(self):
        self.slots = {}

    def create_parking_lot(self, no_of_slots):
        """
        Method to create parking lot with given number
        :param no_of_slots
        :type  Integer
        :return: None
        """
        no_of_slots = int(no_of_slots)

        if len(self.slots) > 0:
            print("Parking Lot already created")
            return None

        if no_of_slots > 0:
            for i in range(1, no_of_slots + 1):
                temp_slot = lot.Lot(slot_no=i, available=True)
                self.slots[i] = temp_slot
            print("Created a parking lot with %s slots" % no_of_slots)
        else:
            print("Number of slots provided is incorrect.")

        return None

    def get_nearest_available_slot(self):
        """
        Get nearest available slot
        :return:
        """
        available_slots = [x for x in list(self.slots.values()) if x.available]
        if not available_slots:
            return None
        return sorted(available_slots, key=lambda x: x.slot_no)[0]

    def park(self, reg_no, colour):
        """
        Method to park car in nearest slot
        Create car object and park in slot
        :param reg_no :type (String)
        :param colour: :type (String)
        :return:
        """

        if not self._pre_checks():
            return

        available_slot = self.get_nearest_available_slot()
        if available_slot:
            available_slot.car = car.Car.create(reg_no, colour)
            available_slot.available = False
            print("Allocated slot number: %s" % available_slot.slot_no)
        else:
            print("Sorry, parking lot is full.")

    def leave(self, slot_no):
        """
        Empty the slot after car left
        :param slot_no :type Integer
        :return:
        """
        slot_no = int(slot_no)
        if not self._pre_checks():
            return

        if slot_no in self.slots:
            pslot = self.slots[slot_no]
            if not pslot.available and pslot.car:
                pslot.car = None
                pslot.available = True
                print("Slot number %s is free" % slot_no)
            else:
                print("No car is present at slot number %s" % slot_no)
        else:
            print("Sorry, slot number does not exist in the parking lot.")

    def status(self):
        """
        parking status
        :return: None
        """
        if not self._pre_checks():
            return

        print("SlotNo \t RegistrationNo \t Colour")
        for i in list(self.slots.values()):
            if not i.available and i.car:
                print("{}\t{}\t{}".format(i.slot_no, i.car.reg_no, i.car.colour))

    def _pre_checks(self):
        if not len(self.slots):
            print("Parking Lot not created")
            return False
        return True

    def registration_numbers_for_cars_with_colour(self, colour):
        """

        :param colour:
        :return:
        """
        if not self._pre_checks():
            return

        reg_nos = ''
        for pslot in list(self.slots.values()):
            if not pslot.available and pslot.car and pslot.car.colour == colour:
                reg_nos += '{}'.format(pslot.car.reg_no)

        if reg_nos:
            print(reg_nos[:-1])
        else:
            print("Not found")

    def slot_numbers_for_cars_with_colour(self, colour):
        """
        slot numbers matching color
        :param colour:
        :type String
        :return:
        """

        if not self._pre_checks():
            return

        slot_nos = ''
        for pslot in list(self.slots.values()):
            if not pslot.available and pslot.car and \
                            pslot.car.colour == colour:
                slot_nos += '%s ' % pslot.slot_no

        if slot_nos:
            print(slot_nos[:-1])
        else:
            print("Not found")

    def slot_number_for_registration_number(self, reg_no):
        """Method to find slot numbers in parking with given registration
        number.
        Input: reg_no - String Type
        """

        if not self._pre_checks():
            return

        slot_no = ''
        for pslot in list(self.slots.values()):
            if not pslot.available and pslot.car and pslot.car.reg_no == reg_no:
                slot_no = pslot.slot_no
                break
        if slot_no:
            print(slot_no)
        else:
            print("Not found")
