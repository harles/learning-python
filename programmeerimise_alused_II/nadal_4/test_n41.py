# Moodultestid üleasndele n41
import unittest
from nadal_4.n41 import yhisosa


class YhisosaTest(unittest.TestCase):

    def test_tulemus_naide1(self):
        self.assertEqual(yhisosa([1, 2], [2, 3]), [2])
    def test_tulemus_naide2(self):
        self.assertEqual(yhisosa(['ich', 'du', 'er', 'sie', 'es'], ['wir', 'ihr', 'sie', 'Sie']), ['sie'])
    def test_tulemus_naide3(self):
        self.assertEqual(yhisosa([], [1, 1]), [])
    def test_tulemus_naide4(self):
        self.assertEqual(yhisosa([1, 1, 1], [1, 1]), [1])
