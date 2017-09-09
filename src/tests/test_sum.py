from unittest import TestCase

import mathfuncs.sum

class TestSum(TestCase):
    def test_is_string(self):
        s = mathfuncs.sum.calculate(2, 5)
        self.assertTrue(isinstance(s, basestring))
        