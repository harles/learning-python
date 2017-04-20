# Moodultestid üleasndele n21
import unittest
from nadal_2.n21 import vahimatest_suurim

class MyTest(unittest.TestCase):


    def test_tulemus_naide1(self):
        self.assertEqual(vahimatest_suurim([[3, 0], [0, -1], [2, 1]]), 1)

    def test_tulemus_naide2(self):
        self.assertEqual(vahimatest_suurim([[3, 0], [0, -1], [2, 2]]), 2)

    def test_tulemus_naide13(self):
        self.assertEqual(vahimatest_suurim([[3, 0]]), 0)

    def test_tulemus_naide14(self):
        self.assertEqual(vahimatest_suurim([[0], [1], [2], [3], [-1]]), 3)

