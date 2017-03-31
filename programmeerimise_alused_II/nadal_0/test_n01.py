# Moodultestid üleasndele n01
import unittest
from nadal_0.n01 import parandatud_tulemus

class MyTest(unittest.TestCase):
    def test_tulemus_standardväärtused(self):
        self.assertEqual(parandatud_tulemus(1.81, 20), 2.01)
    def test_tulemus_üle_kahe_komakoha(self):
        self.assertEqual(parandatud_tulemus(1.0012, 50), 1.50)
