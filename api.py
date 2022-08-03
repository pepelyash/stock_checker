import time
import requests
from requests.exceptions import HTTPError


class ShopApi:
    access_token = None

    def __init__(self, deviceid, app_ver, refresh_token):
        # the function that is executed when an instance of the class is created
        self.deviceid = deviceid
        self.app_ver = app_ver
        self.refresh_token = refresh_token

        if self.is_needtorefresh_access_token():
            try:
                self.access_token = self.get_access_token()
                if self.access_token is None:
                    raise Exception("Request for access token failed.")
            except Exception as e:
                print(e)
            else:
                self.access_token_expiration = int(time.time()) + 300
                print(self.access_token)
                print(self.access_token_expiration)
                # write access token expiration time to file
                with open('tkn_exptime.txt', mode='w', encoding='utf8') as file:
                    file.write(f'{self.access_token_expiration}')
        else:
            raise Exception(f'wait {int(time.time()) - self.access_token_expiration}s before refreshing products list')

    def is_needtorefresh_access_token(self):
        # read access token expiration time from file
        with open('tkn_exptime.txt', mode='r', encoding='utf8') as file:
            self.access_token_expiration = int(file.read())

        if int(time.time()) < self.access_token_expiration:
            return False

        return True

    def get_access_token(self):
        # request an access token
        url = 'https://api.samokat.ru/showcase/oauth/token'
        data = f'grant_type=refresh_token&refresh_token={self.refresh_token}'
        headers = {
            'accept': 'application/json, text/plain, */*',
            'deviceid': self.deviceid,
            'x-application-platform': 'android',
            'x-application-version': self.app_ver,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '103',
            'Host': 'api.samokat.ru',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/4.9.1'
        }
        try:
            response = requests.post(url=url, data=data, headers=headers)

            # optional: raise exception for status code
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            return None
        except Exception as err:
            print(f'Other error occurred: {err}')
            return None
        else:
            # assuming the response's structure is
            # {"access_token": ""}
            return response.json()['access_token']

    def get_products_ids(self, url):
        if self.is_needtorefresh_access_token():
            self.get_access_token()

        headers = {
            'accept': 'application/json, text/plain, */*',
            'authorization': f'Bearer {self.access_token}',
            'x-application-platform': 'android',
            'x-application-version': '3.56.0',
            'Content-Type': 'application/json;charset=utf-8',
            'Content-Length': '2',
            'Host': 'api.samokat.ru',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/4.9.1'
        }
        data = '[]'
        try:
            response = requests.post(url=url, headers=headers, data=data, timeout=10)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            print('failed to get_products_ids')
        except Exception as err:
            print(f'Other error occurred: {err}')
            print('failed to get_products_ids')
        else:
            return response.json()

    def get_products_info(self, url):
        headers = {
            'accept': 'application/json, text/plain, */*',
            'authorization': f'Bearer {self.access_token}',
            'x-application-platform': 'android',
            'x-application-version': '3.56.0',
            'Host': 'api.samokat.ru',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/4.9.1',
            'If-Modified-Since': 'Mon, 01 Aug 2022 13:38:03 GMT'
        }
        data = ''
        try:
            response = requests.get(url=url, headers=headers, data=data, timeout=10)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            print('failed to get_products_info')
        except Exception as err:
            print(f'Other error occurred: {err}')
            print('failed to get_products_info')
        else:
            return response.json()['products']
