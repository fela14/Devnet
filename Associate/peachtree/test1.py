import unittest
import math

def calCircumference(r):
    return 2*r*math.pi

# print (calCircumference(5))

class myTest(unittest.TestCase):
    def test_circumference(self):
        actual = calCircumference(5)
        self.assertEqual(actual, 31.41592653589793)

    def test_cicumZero(self):
        actual = calCircumference(0)
        self.assertEqual(actual, 0)

unittest.main()

