# Moodultestid üleasndele n21
import unittest
from nadal_2.n22 import on_bingo_tabel
from nadal_2.n22 import kontrolli_veergu


class MyTest(unittest.TestCase):
    def test_veerg1_algus(self):
        self.assertEqual(kontrolli_veergu(0,1), True)

    def test_veerg1_lopp(self):
        self.assertEqual(kontrolli_veergu(0, 15), True)

    def test_veerg1_lopp_ule(self):
        self.assertEqual(kontrolli_veergu(0, 16), False)

    def test_tulemus_naide1(self):
        self.assertEqual(on_bingo_tabel([[1, 30, 34, 55, 75], [10, 16, 40, 50, 67], [5, 20, 38, 48, 61], [4, 26, 43, 49, 70], [15, 17, 33, 51, 66]]), True)

    def test_tulemus_naide2(self):
        self.assertEqual(on_bingo_tabel([[1, 30, 34, 55, 76], [10, 16, 40, 50, 67], [5, 20, 38, 48, 61], [4, 26, 43, 49, 70], [15, 17, 33, 51, 66]]), False)