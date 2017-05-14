# Moodultestid üleasndele n63
import unittest
from nadal_6.n63 import pikim_pikkus


class PikimPikkusTest(unittest.TestCase):

    def test_tulemus_naide1(self):
        self.assertEqual(pikim_pikkus([1, 2, 3]), 3)

    def test_tulemus_naide2(self):
        self.assertEqual(pikim_pikkus([[[1, 2, 3]]]), 3)

    def test_tulemus_naide3(self):
        self.assertEqual(pikim_pikkus([[], [3, [4, 5], [2, 3, 4, 5, 3, 3], [7], 5, [1, 2, 3], [3, 4]], [1, 2, 3, 4, 5]])
                         , 7)

    def test_tulemus_naide4(self):
        self.assertEqual(pikim_pikkus([[], []]), 2)

    def test_tulemus_naide5(self):
        self.assertEqual(pikim_pikkus([]), 0)

    def test_tulemus_naide6(self):
        self.assertEqual(pikim_pikkus([[[[[]]]]]), 1)
