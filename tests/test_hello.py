import unittest
import sys
from io import StringIO  # For capturing stdout
from seav import hello

class TestHello(unittest.TestCase):
    def test_say_hello(self):
        # Create a StringIO object to capture the printed output
        captured_output = StringIO()
        original_stdout = sys.stdout
        sys.stdout = captured_output
        
        # Call the function that prints "Hello World"
        hello.say_hello()
        
        # Get the printed output and restore the original stdout
        printed_output = captured_output.getvalue()
        sys.stdout = original_stdout
        
        # Assert that the printed output is as expected
        expected_output = "Hello World\n"  # Include the newline character
        self.assertEqual(printed_output, expected_output)

if __name__ == '__main__':
    unittest.main()