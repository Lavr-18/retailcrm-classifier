import unittest
from classifier import classify_lead


class TestClassifier(unittest.TestCase):
    def test_high_value_today(self):
        data = {'totalSumm': 60000, 'dostavka_do': '2025-05-21'}
        self.assertEqual(classify_lead(data), 'AA')

    def test_low_value_late(self):
        data = {'totalSumm': 15000, 'dostavka_do': '2025-07-01'}
        self.assertEqual(classify_lead(data), 'CC')

    def test_d_category(self):
        data = {'totalSumm': 400000, 'dostavka_do': '2025-07-25'}
        self.assertEqual(classify_lead(data), 'D')
