# Moodultestid üleasndele n44a
import unittest
from nadal_4.n44a import on_alglopuline


class OnAlglopulineTest(unittest.TestCase):

    def test_tulemus_naide1(self):
        self.assertEqual(on_alglopuline([4, 3, 2]), True)

    def test_tulemus_naide2(self):
        self.assertEqual(on_alglopuline([-1, 0]), False)

    def test_tyhi(self):
        self.assertEqual(on_alglopuline([]), False)