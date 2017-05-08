# Moodultestid üleasndele n42
import unittest
from nadal_4.n42 import listid_sonastikuks


class ListSonastikuksTest(unittest.TestCase):

    def test_tulemus_naide1(self):
        self.assertEqual(listid_sonastikuks([1, 2], [3, 4]), {1: 3, 2: 4})

    def test_tulemus_naide2(self):
        self.assertEqual(listid_sonastikuks(['ATI', 'KAMA'], ['Arvutiteaduse instituut', 'Kasutatav masintõlge']),
                         {'KAMA': 'Kasutatav masintõlge', 'ATI': 'Arvutiteaduse instituut'})

    def test_tulemus_naide3(self):
        self.assertEqual(listid_sonastikuks([], []), {})

    def test_tulemus_naide4(self):
        self.assertEqual(listid_sonastikuks([0, 1, 0], ['a', 'b', 'c']), {0: 'c', 1: 'b'})
