import unittest
from translator import english_to_french, french_to_english

class TestFr2En(unittest.TestCase):
    """test case for french to english"""
    def test1(self):
        # test case text 
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french(None), None)

class TestEn2Fr(unittest.TestCase):
    """test case for englsih to french"""
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english(None), None)

unittest.main()