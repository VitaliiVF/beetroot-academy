import unittest

from example_func import is_pangram
from example_func import validate_pin

class NameTestCase(unittest.TestCase):
    
    def test_is_pangram(self):
        pangram = is_pangram("abcdefghijklmnopqrstuvwxyz")
        pangram2 = is_pangram("acdefghijklmnopqrstuvwxyz")
        self.assertEqual(pangram, True)
        self.assertEqual(pangram2, False)
        
    def test_validate_pin(self):
        pin = validate_pin("re12")
        pin2 = validate_pin("1244")
        self.assertEqual(pin, False)
        self.assertEqual(pin2, True)
        
unittest.main()