import requests
from requests.exceptions import HTTPError


def get_access_token(session):
    url = 'https://api.samokat.ru/showcase/oauth/token'
    refresh_token = '49134d2d6601e5a52d325127322757a522755d77292e8dbf2a46104426cd4ca5'
    data = f'grant_type=refresh_token&refresh_token={refresh_token}'  # copy-paste refresh_token from opened app
    deviceid = 'db24b4f9760fc4ea'
    app_ver = '3.56.0'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'deviceid': deviceid,
        'x-application-platform': 'android',
        'x-application-version': app_ver,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '103',
        'Host': 'api.samokat.ru',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/4.9.1'
    }
    access_token = ''
    try:
        response = session.post(url=url, data=data, headers=headers)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        if response.status_code == 200:
            access_token = response.json()['access_token']
    return access_token


def get_product_ids(session, access_token):
    url = 'https://api.samokat.ru/showcase/showcases/de1c674b-ddda-4485-9b7c-e13f5e901088/stocks'
    authorization = f'Bearer {access_token}'
    # print(authorization)
    headers = {
        'accept': 'application/json, text/plain, */*',
        'authorization': authorization,
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
        response = session.post(url=url, headers=headers, data=data, timeout=10)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        return response.json()


def get_products_price(session, access_token):
    url = 'https://api.samokat.ru/showcase/showcases/de1c674b-ddda-4485-9b7c-e13f5e901088?version=0'
    authorization = f'Bearer {access_token}'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'authorization': authorization,
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
        response = session.get(url=url, headers=headers, data=data, timeout=10)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        return response.json()['products']


def get_products_data():
    with requests.Session() as s:
        access_token = get_access_token(s)
        if not access_token:
            return print('failed to get access_token')
        print(access_token)
        product_ids = get_product_ids(s, access_token)
        if not product_ids:
            return print('failed to get product_ids list')
        products_price = get_products_price(s, access_token)
        if not products_price:
            return print('failed to get products_price list')
        return product_ids, products_price


def main():
    return get_products_data()


if __name__ == '__main__':
    main()
