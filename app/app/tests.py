"""
Sample test
"""

from django.test import SimpleTestCase
from . import calc


class CalcTest(SimpleTestCase):
    """ Test calc function """
    def test_add_function(self):
        """Test additing numbers together"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract(self):
        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)
