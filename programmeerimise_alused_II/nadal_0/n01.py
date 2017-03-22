# Kursuse kontrollülesanne
# Allikas: https://courses.cs.ut.ee/2017/eprogalused2/spring/Main/Kontrollylesanne
import unittest


def parandatud_tulemus(vigane_tulemus_m, mõõteparandus_cm):
    tegelik_tulemus = round(vigane_tulemus_m + mõõteparandus_cm/100, 2)
    return tegelik_tulemus

print(parandatud_tulemus(1.1, 35))


class MyTest(unittest.TestCase):
    def test_tulemus_standardväärtused(self):
        self.assertEqual(parandatud_tulemus(1.81, 20), 2.01)

    def test_tulemus_üle_kahe_komakoha(self):
        self.assertEqual(parandatud_tulemus(1.0012, 50), 1.50)
