import requests
from requests.exceptions import HTTPError
import os


def get_access_token(session):
    url = 'https://api.samokat.ru/showcase/oauth/token'
    data = f'grant_type=refresh_token&refresh_token={os.getenv("refresh_token")}'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'deviceid': os.getenv('deviceid'),
        'x-application-platform': 'android',
        'x-application-version': os.getenv('app_ver'),
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
        response = session.post(url=os.getenv('product_ids_url'), headers=headers, data=data, timeout=10)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        return response.json()


def get_products_price(session, access_token):
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
        response = session.get(url=os.getenv('products_price_url'), headers=headers, data=data, timeout=10)
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
