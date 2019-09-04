#!/usr/bin/python
import os
import sys

from logic.parking import Parking


class Commands(object):
    """
    class to handle command line operations
    """

    def __init__(self):
        self.parking = Parking()

    @staticmethod
    def script_usage():
        """
        script usage
        :return:
        """
        print("""
            Usage(commands):
                create_parking_lot <number>
                park <car number> <colour>
                leave <parked_number>
                status
                registration_numbers_for_cars_with_colour <colour>
                slot_numbers_for_cars_with_colour <colour>
                slot_number_for_registration_number <car_number>
              """)

    def process_file(self, command_file):
        """
        read input command file
        :param command_file: filepath
        :return:
        """
        if not os.path.exists(command_file):
            print("Given file {} does not exist".format(command_file))

        try:
            with open(command_file, 'r') as file_obj:
                for line in file_obj:
                    if line != '\n':
                        self.process_command(line)

        except Exception as ex:
            print("Error occurred while processing input file {}".format(ex))

    def process_input(self):
        print("Interactive mode:")
        self.script_usage()
        try:
            while True:
                stdin_input = input("Enter command: ")
                self.process_command(stdin_input)

        except (KeyboardInterrupt, SystemExit):
            return

        except Exception as ex:
            print("Error occured while processing input {}".format(ex))

    def process_command(self, stdin_input):
        inputs = stdin_input.split()
        command = inputs[0]
        params = inputs[1:]

        if hasattr(self.parking, command):
            command_function = getattr(self.parking, command)
            command_function(*params)
        else:
            print("Got wrong command.")


if __name__ == "__main__":
    # main script to call backend script
    args = sys.argv

    if len(args) == 1:
        p_command = Commands()
        p_command.process_input()

    elif len(args) == 2:
        p_command = Commands()
        p_command.process_file(args[1])

    else:
        print("""
            Wrong number of arguments.
            Usage:
                ./parking_lot.py <filename> OR
                ./parking_lot.py
            """)
