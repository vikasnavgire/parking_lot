# Setup (prerequisites)

1. Install python3* (DEV used Python 3.5.2 (default, Nov 12 2018, 13:43:14) [GCC 5.4.0 20160609] on linux)
2. create venv (virtualenv venv) - optional
3. activate venv (source venv/bin/activate) - optional

cd parking_lot

1. start application in interactive mode:
     $ ./bin/parking_lot

2. Start application and execute commands from input.text file
     $ ./bin/parking_lot functional_spec/fixtures/file_input.txt

# Usage
        create_parking_lot <number>
        park <car number> <colour>
        leave <parked_number>
        status
        registration_numbers_for_cars_with_colour <colour>
        slot_numbers_for_cars_with_colour <colour>
        slot_number_for_registration_number <car_number>


# Functional Suite
cd parking_lot and run ./bin/setup
or
python -m unittest discover


# Development References
1. Python PEP8 coding standards followed
   https://www.python.org/dev/peps/pep-0008/
2. python.org used for references
   https://docs.python.org/3/
