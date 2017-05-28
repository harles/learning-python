# Moodultestid üleasndele sla
import unittest
from nadal_7.sla import paevikuus
from nadal_7.sla import minuteidkuus



class PaeviKuusTest(unittest.TestCase):

    def test_2017juuni(self):
        self.assertEqual(paevikuus(2017, 6), 30)
    def test_2017juuli(self):
        self.assertEqual(paevikuus(2017, 7), 31)
    def test_2016eebruar(self):
        self.assertEqual(paevikuus(2016, 2), 29)

class MinuteidKuusTest(unittest.TestCase):
    def test_2017juuni(self):
        self.assertEqual(minuteidkuus(2017, 6), 43200)