# Moodultestid üleasndele n52
import unittest
from nadal_5.n52 import paarissumma


class PaarissummaTest(unittest.TestCase):

    def test_tulemus_naide1(self):
        self.assertEqual(paarissumma(1), 0)
    def test_tulemus_naide2(self):
        self.assertEqual(paarissumma(2), 2)
    def test_tulemus_naide3(self):
        self.assertEqual(paarissumma(3), 2)
    def test_tulemus_naide4(self):
        self.assertEqual(paarissumma(100), 2550)
    def test_tulemus_naide5(self):
        self.assertEqual(paarissumma(101), 2550)
