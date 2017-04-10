# Moodultestid üleasndele n11
import unittest
from nadal_1.n11 import kala_kaal

class MyTest(unittest.TestCase):
    def test_tulemus_naide1(self):
        self.assertEqual(kala_kaal(70, 0.19), 652)
    def test_tulemus_üle_kahe_komakoha(self):
        self.assertEqual(kala_kaal(12, 1.34), 23)