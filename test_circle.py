import unittest
from circle import circle_area
from math import pi

class TestCircleAarea(unittest.TestCase):
    def test_area(self):
        
        self.assertAlmostEqual(circle_area(0),0)
        #self.assertAlmostEqual(circle_area(2.1),pi*2.1**2)
    def test_values(self):
        self.assertRaises(ValueError,circle_area,-2)