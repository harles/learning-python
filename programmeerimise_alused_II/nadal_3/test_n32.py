# Moodultestid üleasndele n32
import unittest
from nadal_3.n32 import tahised_nimedeks


class TahisedNimedeksTest(unittest.TestCase):


    def test_tulemus_naide1(self):
        self.assertEqual(tahised_nimedeks(['FIN', 'RUS', 'CHN', 'IND', 'F', 'LAO'],
                                          {'J': 'Jaapan', 'SGP': 'Singapur', 'IND': 'India', 'LAO': 'Laos', 'T': 'Tai',
                                           'CHN': 'Hiina'}),
                         [None, None, 'Hiina', 'India', None, 'Laos'])