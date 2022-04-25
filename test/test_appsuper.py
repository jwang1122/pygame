import unittest
from src.appsuper import *

class TestFunction(unittest.TestCase):

    def test_randomPoint(self):
        for i in range(1000):
            point = randomPoint()
            self.assertTrue(point[0] <= 600)
            self.assertTrue(point[1] <= 440)