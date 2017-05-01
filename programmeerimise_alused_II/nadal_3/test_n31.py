# Moodultestid üleasndele n31
import unittest
from nadal_3.n31 import symbolite_sagedus


class SymboliteSagedusTest(unittest.TestCase):


    def test_tulemus_naide1(self):
        self.assertEqual(symbolite_sagedus("Hommikul silmad on kinni ja huulil on naer"),
                         {'H': 1, 'o': 3, 'm': 3, 'i': 5, 'k': 2, 'u': 3, 'l': 4, ' ': 7, 's': 1, 'a': 3, 'd': 1,
                          'n': 5, 'j': 1, 'h': 1, 'e': 1, 'r': 1})

    def test_tulemus_naide2(self):
        self.assertEqual(symbolite_sagedus("suitsupääsuke"),
                         {'s': 3, 'u': 3, 'i': 1, 't': 1, 'p': 1, 'ä': 2, 'k': 1, 'e': 1})

    def test_tulemus_naide3(self):
        self.assertEqual(symbolite_sagedus("l@htek00d"),
                         {'l': 1, '@': 1, 'h': 1, 't': 1, 'e': 1, 'k': 1, '0': 2, 'd': 1})
