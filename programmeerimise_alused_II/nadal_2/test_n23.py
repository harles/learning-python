# Moodultestid üleasndele n23
import unittest
from nadal_2.n23 import voitis_nurkademangu
from nadal_2.n23 import x_peadiagonaalil
from nadal_2.n23 import x_korvaldiagonaalil
from nadal_2.n23 import voitis_diagonaalidemangu
from nadal_2.n23 import voitis_taismangu

class NurkademangVoitTests(unittest.TestCase):
    def test_voitis_nurkademangu_voit(self):
        self.assertEqual(voitis_nurkademangu([['X', 30, 34, 55, 'X'],
                                              [10, 16, 40, 50, 67],
                                              [5, 20, 38, 48, 61],
                                              [4, 26, 43, 49, 70],
                                              ['X', 17, 33, 51, 'X']]),
                                               True)

    def test_voitis_nurkademangu_tuhipilet(self):
        self.assertEqual(voitis_nurkademangu([[1, 30, 34, 55, 75],
                                              [10, 16, 40, 50, 67],
                                              [5, 20, 38, 48, 61],
                                              [4, 26, 43, 49, 70],
                                              [15, 17, 33, 51, 66]]),
                                               False)

    def test_voitis_nurkademangu_poolik(self):
        self.assertEqual(voitis_nurkademangu([['X', 30, 34, 55, 75],
                                              [10, 16, 40, 50, 67],
                                              [5, 20, 38, 48, 61],
                                              [4, 'X', 43, 49, 70],
                                              [15, 17, 33, 51, 'X']]),
                                               False)


class XPeadiagonaalilTests(unittest.TestCase):
    def test_X_arv_peadiagonaalil_aarmised(self):
        self.assertEqual(x_peadiagonaalil([['X', 30, 34, 55, 'X'],
                                              [10, 16, 40, 50, 67],
                                              [5, 20, 38, 48, 61],
                                              [4, 26, 43, 49, 70],
                                              ['X', 17, 33, 51, 'X']]),
                                                2)

    def test_X_arv_peadiagonaalil_terverida(self):
        self.assertEqual(x_peadiagonaalil([['X', 30, 34, 55, 'X'],
                                           [10, 'X', 40, 50, 67],
                                           [5, 20, 'X', 48, 61],
                                           [4, 26, 43, 'X', 70],
                                           ['X', 17, 33, 51, 'X']]),
                                             5)

    def test_X_arv_peadiagonaalil_puuduvad(self):
        self.assertEqual(x_peadiagonaalil([[1, 30, 34, 55, 75],
                                              [10, 16, 40, 50, 67],
                                              [5, 20, 38, 48, 61],
                                              [4, 26, 43, 49, 70],
                                              [15, 17, 33, 51, 66]]),
                                               0)


class XKorvaldiagonaalilTests(unittest.TestCase):
    def test_X_arv_korvaldiagonaalil_aarmised(self):
        self.assertEqual(x_korvaldiagonaalil([['X', 30, 34, 55, 'X'],
                                           [10, 16, 40, 50, 67],
                                           [5, 20, 38, 48, 61],
                                           [4, 26, 43, 49, 70],
                                           ['X', 17, 33, 51, 'X']]),
                                            2)

    def test_X_arv_korvaldiagonaalil_terverida(self):
        self.assertEqual(x_korvaldiagonaalil([[1, 30, 34, 55, 'X'],
                                           [10, 16, 40, 'X', 67],
                                           [5, 20, 'X', 48, 61],
                                           [4, 'X', 43, 49, 70],
                                           ['X', 17, 33, 51, 66]]),
                                             5)

    def test_X_arv_korvaldiagonaalil_puuduvad(self):
        self.assertEqual(x_korvaldiagonaalil([[1, 30, 34, 55, 75],
                                           [10, 16, 40, 50, 67],
                                           [5, 20, 38, 48, 61],
                                           [4, 26, 43, 49, 70],
                                           [15, 17, 33, 51, 66]]),
                                            0)

class VoitisDiagonaalidemanguTests(unittest.TestCase):
    def test_kaks_taisdiagonaali(self):
        self.assertEqual(voitis_diagonaalidemangu([['X', 30, 34, 55, 'X'],
                                              [ 10, 'X', 40, 'X', 67],
                                              [  5, 20, 'X', 48, 61],
                                              [  4, 'X', 43, 'X', 70],
                                              ['X', 17, 33, 51, 'X']]),
                                               True)

    def test_korvaldiagonaal(self):
        self.assertEqual(voitis_diagonaalidemangu([[1, 30, 34, 55, 'X'],
                                              [10, 16, 40, 'X', 67],
                                              [5, 20, 'X', 48, 61],
                                              [4, 'X', 43, 49, 70],
                                              ['X', 17, 33, 51, 66]]),
                                               False)


class VoitisTaismanguTests(unittest.TestCase):
    def test_taismangu_voit(self):
        self.assertEqual(voitis_taismangu([['X', 'X', 'X', 'X', 'X'],
                                              [ 'X', 'X', 'X', 'X', 'X'],
                                              [  'X', 'X', 'X', 'X', 'X'],
                                              [  'X', 'X', 'X', 'X', 'X'],
                                              ['X', 'X', 'X', 'X', 'X']]),
                                               True)

    def test_ei_voitnud_taismangu(self):
        self.assertEqual(voitis_taismangu([[1, 30, 34, 55, 'X'],
                                              [10, 16, 40, 'X', 67],
                                              [5, 20, 'X', 48, 61],
                                              [4, 'X', 43, 49, 70],
                                              ['X', 17, 33, 51, 66]]),
                                               False)
