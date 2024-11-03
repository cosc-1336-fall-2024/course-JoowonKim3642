#test

import unittest
from src.homework.g_lists_and_tuples.lists import get_lowest_list_value, get_highest_list_value

class Test_Config(unittest.TestCase):

    def test_lowest_list_value(self):
        numbers = [8, 10, 1, 50, 20]
        self.assertEqual(1, get_lowest_list_value(numbers))

    def test_highest_list_value(self):
        numbers = [8, 10, 1, 50, 20]
        self.assertEqual(50, get_highest_list_value(numbers))