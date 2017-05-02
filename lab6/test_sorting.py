from unittest import TestCase
from is_sorted import *


class TestLine_intersect(TestCase):
    def test_sorting(self):
        self.assertEquals(print(is_sorted([1, 2, 3, 4, 4, 5, 6]), True))
        self.assertEquals(print(is_sorted([1, 2, 3, 4, 4, 5, 5]), True))
        self.assertEquals(print(is_sorted([1, 2, 3, 4, 4, 5, 2]), False))
        self.assertEquals(print(is_sorted([]), True))
        self.assertEquals(print(is_sorted([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]), True))
