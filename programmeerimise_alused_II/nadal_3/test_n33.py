# Moodultestid üleasndele n33
import unittest
from nadal_3.n33 import vordle_lubadusi
from nadal_3.n33 import kooslubajad


class LubadusteVordlusTest(unittest.TestCase):
    def test_kaks_lubadust(self):
        self.assertEqual(vordle_lubadusi([{"maamaks kaotada", "pensione tõsta", "kaitsekulutusi tõsta"},
                                      {"maamaks kaotada"}]), [[0, 1, 1]])

    def test_kolm_lubadust(self):
        self.assertEqual(vordle_lubadusi([{"maamaks kaotada", "pensione tõsta", "kaitsekulutusi tõsta"},
                                          {"maamaks kaotada"},
                                          {"pensione tõsta", "kaitsekulutusi tõsta"}]),
                         [[0, 1, 1], [0, 2, 2], [1, 2, 0]])

    def test_kaks_lubadust_kontrollist(self):
        self.assertEqual(vordle_lubadusi([{'kuritegevust vähendada', 'rajada spordiväljakud igasse linna',
                                           'kaotada kõik maksud', 'algatada koduloometoetus',
                                           'suurendada kõiki palkasid', 'kõiki toetusi suurendada'},
                                          {'vähendada suremust', 'toetada pensionäre', 'suurendada vastsündinute arvu',
                                           'edendada maaelu', 'aidata noorperesid'}]),
                                         [[0, 1, 0]])


class KooslubajadTest(unittest.TestCase):


    def test_tulemus_naide1(self):
        self.assertEqual(kooslubajad([{"maamaks kaotada", "pensione tõsta", "kaitsekulutusi tõsta"},
                                      {"lasteaiaõpetajate palku tõsta", "kindlustada tasuta hambaravi kuni 30-aastastele"},
                                      {"sisserännet piirata", "pensione tõsta", "kaitsekulutusi tõsta"}, set()]),
                         (0, 2))

    def test_tulemus_naide3(self):
        self.assertEqual(kooslubajad([{'kuritegevust vähendada', 'rajada spordiväljakud igasse linna',
                                        'kaotada kõik maksud', 'algatada koduloometoetus', 'suurendada kõiki palkasid',
                                        'kõiki toetusi suurendada'},
                                       {'vähendada suremust', 'toetada pensionäre', 'suurendada vastsündinute arvu',
                                        'edendada maaelu', 'aidata noorperesid'}]),
                         (0, 1))
