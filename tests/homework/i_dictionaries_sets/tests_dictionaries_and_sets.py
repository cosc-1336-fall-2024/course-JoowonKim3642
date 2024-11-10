#test

import unittest
from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget

class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
        inventory = {}
        
        add_inventory(inventory, "Widget1", 10)
        self.assertEqual({"Widget1":10}, inventory)

        add_inventory(inventory, "Widget1", 25)
        self.assertEqual({"Widget1":35}, inventory)

        add_inventory(inventory, "Widget1", -10)
        self.assertEqual({"Widget1":25}, inventory)


    def test_remove_inventory_widget(self):
        inventory2 = {}

        add_inventory(inventory2, "Widget1", 10)
        add_inventory(inventory2, "Widget2", 5)
        remove_inventory_widget(inventory2, "Widget1")

        self.assertEqual(len(inventory2), 1)
        self.assertNotIn("Widget1", inventory2)
        self.assertIn("Widget2", inventory2)