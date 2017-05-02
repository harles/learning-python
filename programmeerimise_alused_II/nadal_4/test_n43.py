# Moodultestid üleasndele n42
import unittest
from nadal_4.n43 import absoluutne_tabel


class AbsoluutneTabelTest(unittest.TestCase):

    def test_tulemus_naide1(self):
        self.assertEqual(absoluutne_tabel([[1, -2], [-3, 4]]), [[1, 2], [3, 4]])
