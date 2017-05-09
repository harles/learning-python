# Moodultestid üleasndele n53a
import unittest
from nadal_5.n53a import dissonantside_arv


class DissonantsideArvTest(unittest.TestCase):

    def test_tulemus_naide1(self):
        self.assertEqual(dissonantside_arv([1, 4], 2), 0)

    def test_tulemus_naide2(self):
        self.assertEqual(dissonantside_arv([-1, 3], 4), 0)

    def test_tulemus_naide3(self):
        self.assertEqual(dissonantside_arv([-1, 3], 3), 1)

    def test_tulemus_naide4(self):
        self.assertEqual(dissonantside_arv([0, 3], 1), 0)

    def test_tulemus_naide5(self):
        self.assertEqual(dissonantside_arv([1, 4, 0, -10, -1, 3, 42], 2), 1)

    def test_tulemus_naide6(self):
        self.assertEqual(dissonantside_arv([1, -3, 1, 0, 0, -2, -3, 3, -3, 12], 3), 5)

