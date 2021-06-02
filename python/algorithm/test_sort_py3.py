import unittest
import random

from . import sort_algo

class TestSort(unittest.TestCase):
    def setUp(self):
        no_equal = list(range(10))
        with_equal = no_equal[:]
        with_equal.extend(with_equal)
        with_equal.sort()
        self.lists_sorted = [no_equal, with_equal]

    def compare(self, sort_in_place_func, times=1000):
        for sorted_one in self.lists_sorted:
            for x in range(times):
                l_copy = sorted_one[:]
                while sorted_one == l_copy:
                    random.shuffle(l_copy)

                sort_in_place_func(l_copy)
                self.assertTrue(sorted_one == l_copy)

    def test_bubble(self):
        self.compare(sort_algo.bubble)

    def test_bubble_recursive(self):
        self.compare(sort_algo.bubble_recursive_py3)
