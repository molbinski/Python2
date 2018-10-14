#tester@tester-m:~/spotkanie2/unitest$ cat test.py

import unittest

from calculator import calculate
from calculator import str_calculator

class TestCalcurator(unittest.TestCase):
    def test_dodawanie(self):
        r = calculate(1, 2, '+')
        self.assertEqual(r, 3)
    def test_odejmowanie(self):
        r = calculate(4,2,'-')
        self.assertEqual(r, 2)
    def test_mnozenie(self):
        r = calculate(4, 3, "*")
        self.assertEqual(r, 12)
    def test_dzielenie(self):
        r = calculate(10, 2, "/")
        self.assertEqual(r, 5)

class TestStringCalculator(unittest.TestCase):
    def test_concat(self):
        r = str_calculator('t', 2, "+")
        self.assertEqual = (r, 'tt')
    def test_in(self):
        r = str_calculator("glob","hemoglobina", "in")
        self.assertEqual(r, True)
