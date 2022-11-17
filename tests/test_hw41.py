import unittest
from parameterized import parameterized
from hw4_1 import filter_logs

FIXTURE = [
    ('Россия', [{'visit1': ['Москва', 'Россия']},
                {'visit3': ['Владимир', 'Россия']},
                {'visit7': ['Тула', 'Россия']},
                {'visit8': ['Тула', 'Россия']},
                {'visit9': ['Курск', 'Россия']},
                {'visit10': ['Архангельск', 'Россия']}]
     ),
    ('Португалия', [{'visit4': ['Лиссабон', 'Португалия']},
                    {'visit6': ['Лиссабон', 'Португалия']}]
     )
]

class TestFunc(unittest.TestCase):
    @parameterized.expand(FIXTURE)
    def test_hw41(self, country, etalon):
        result = filter_logs(country)
        self.assertEqual(result, etalon)

