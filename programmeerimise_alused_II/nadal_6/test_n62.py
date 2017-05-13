# Moodultestid üleasndele n62
import unittest
from nadal_6.n62 import kuup


class KuupTest(unittest.TestCase):

    def test_tulemus_naide1(self):
        self.assertEqual(kuup([]), [])
    def test_tulemus_naide2(self):
        self.assertEqual(kuup([0, 1, 3]), [0, 1, 27])
