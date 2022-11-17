import requests

def create_folder(data_token,foldername):
    with open(data_token, 'r') as file_object:
        token_ya = file_object.read().strip()

    class Ya:

        def __init__(self, token):
            assert isinstance(token, object)
            self.token = token

        def get_headers(self):
            return {
                'Content-Type': 'application/json',
                'Authorization': f'OAuth {self.token}'
            }

        def newfolder(self, folder_name: str):
            url = 'https://cloud-api.yandex.net/v1/disk/resources'
            headers = self.get_headers()
            params = {"path": folder_name}
            requests.put(url, headers=headers, params=params)

    one = Ya(token_ya)
    one.newfolder(foldername)

create_folder('token_ya.txt','testfolder')

