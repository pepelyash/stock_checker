import time
from dotenv import load_dotenv
import os
from api import ShopApi


def get_products_list():
    new_request = ShopApi(os.getenv('deviceid'), os.getenv('app_ver'), os.getenv('refresh_token'))
    ids = new_request.get_products_ids(os.getenv('products_ids_url'))
    print(ids)
    prices = new_request.get_products_prices(os.getenv('products_prices_url'))
    print(prices)


def main():
    get_products_list()
    pass


if __name__ == '__main__':
    # track program execution time
    start_ts = time.time()
    print(f'launch time: {time.strftime("%I:%M %p")}')
    load_dotenv()   # load environment variables from .env file
    main()
    print(f'execution time: {time.time() - start_ts}')
