import io
import sys
import unittest
from unittest.mock import patch

from logic.main import Commands
from test.test_variables import *


class TestCommands(unittest.TestCase):
    def setUp(self):
        self.cmd_obj = Commands()
        self.capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = self.capturedOutput

    def tearDown(self): pass

    def test_script_usage(self):
        self.cmd_obj.script_usage()
        sys.stdout = sys.__stdout__
        self.capturedOutput.getvalue()
        self.assertIsNotNone(self.capturedOutput.getvalue())

    def test_process_file(self):
        input_file = 'test_file_input.txt'
        self.cmd_obj.process_file(input_file)
        sys.stdout = sys.__stdout__
        print(self.capturedOutput.getvalue())
        self.assertIsNotNone(self.capturedOutput.getvalue())

    def test_process_file_not_found(self):
        input_file = 'test_file_input.txt1'
        self.cmd_obj.process_file(input_file)
        sys.stdout = sys.__stdout__
        # print(self.capturedOutput.getvalue())
        self.assertIsNotNone(self.capturedOutput.getvalue())

    @patch('builtins.input')
    def test_process_input(self, mock_input):
        mock_input.side_effect = ['create_parking_lot 3', 'park MH12AU1336 black', 'leave 1', '\n']
        self.cmd_obj.process_input()
        sys.stdout = sys.__stdout__
        # print(self.capturedOutput.getvalue())
        self.assertIsNotNone(self.capturedOutput.getvalue())

    def test_process_command(self):
        cmd = "status"
        self.cmd_obj.process_command(cmd)
        sys.stdout = sys.__stdout__
        self.assertEqual(self.capturedOutput.getvalue(), status_test)

    def test_process_command_invalid(self):
        cmd = "status1"
        self.cmd_obj.process_command(cmd)
        sys.stdout = sys.__stdout__
        self.assertEqual(self.capturedOutput.getvalue(), wrong_cmd)


if __name__ == '__main__':
    unittest.main()
