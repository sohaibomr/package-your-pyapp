from unittest import TestCase

import mathfuncs.advance.product

class TestSquare(TestCase):
    def testsquare(self):
        expected = 4
        actual = mathfuncs.advance.product.calculate(2, 2)
        self.assertEqual(expected, actual)
        
