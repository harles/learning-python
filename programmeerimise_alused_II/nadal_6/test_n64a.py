# Moodultestid üleasndele n64a
import unittest
from nadal_6.n64a import kes_on


class KesOnTest(unittest.TestCase):

    def test_tulemus_naide1(self):
        self.assertEqual(kes_on(54125632, [(4710209, 'Ernst'), (54125632, 'Uno'), (6524256, 'Arvo')]), 'Uno')

    def test_tulemus_naide2(self):
        self.assertEqual(kes_on(5107261, [(4710209, 'Ernst'), (6524256, 'Arvo')]), None)

    def test_tulemus_tuhiraamat(self):
        self.assertEqual(kes_on(5107261, []), None)
