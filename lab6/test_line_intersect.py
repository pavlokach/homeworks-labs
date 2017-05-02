from unittest import TestCase
from line_intersect import *


class TestLine_intersect(TestCase):
    def test_line_intersect(self):
        self.assertEquals(line_intersect(((0, 0), (2, 1)), ((0, 1), (2, 0))), (1.0, 0.5))
        self.assertEquals(line_intersect(((0, 0), (0, 1)), ((0, 1), (0, 2))), ((0, 0), (0, 1)))
        self.assertEquals(line_intersect(((0, 0), (2, 1)), ((0, 1), (10, 0))), (1.667, 0.833))
        self.assertEquals(line_intersect(((0, 0), (0, 1)), ((1, 0), (1, 1))), None)
        self.assertEquals(line_intersect(((0, 0), (0, 2)), ((1, 0), (1, 12))), None)
        self.assertEquals(line_intersect(((0, 26), (0, 52)), ((75, 0), (75, 12))), None)
