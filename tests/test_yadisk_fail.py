import unittest
from parameterized import parameterized
import requests
from ya_disk import create_folder

FIXTURE = [
    ('token_ya.txt', 'testfolder', 400),
    ('token_ya.txt', 'testfolder', 201),
    ('token_ya.txt', 'testfolder', 402)

]

class TestFunc(unittest.TestCase):

    @parameterized.expand(FIXTURE)
    @unittest.expectedFailure
    def test_yadisk(self, data_token, foldername, etalon):
        create_folder(data_token, foldername)

        with open(data_token, 'r') as file_object:
            token_ya = file_object.read().strip()

        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': token_ya
        }
        params = {"path": foldername}
        response = requests.get(url, headers=headers, params=params)
        result = response.status_code
        requests.delete(url, headers=headers, params=params)


        self.assertEqual(result, etalon)






