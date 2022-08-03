import time
from dotenv import load_dotenv
import os
from api import ShopApi
import sortby


def get_products():
    # get products_ids amd products_info from different requests
    new_request = ShopApi(os.getenv('deviceid'), os.getenv('app_ver'), os.getenv('refresh_token'))
    # first response carries products_ids and its quantity
    products_ids = new_request.get_products_ids(os.getenv('products_ids_url'))
    # second response carries products_info like name, price, picture, etc.
    products_info = new_request.get_products_info(os.getenv('products_info_url'))

    # merge products_ids and products_info by product_id
    for item in products_info:
        if item in products_ids:
            products_info[item]['quantity'] = products_ids[item]['quantity']
            products_info[item]['totalcost'] = int(products_info[item]['price']*products_info[item]['quantity']/100)
        else:
            # set basic values so sort functions don't crash
            products_info[item]['quantity'] = 0
            products_info[item]['totalcost'] = 0

    return products_info


def main():
    items = get_products()

    # save merged info into file
    sortby.save_to_file(items)
    sortby.totalcost_670to630_desc(items)
    sortby.price_asc(items)
    sortby.biggest_discount(items)

    # # load items from existing file
    # items = sortby.load_from_file()
    # sortby.totalcost_670to630_desc(items)
    # sortby.price_asc(items)
    # sortby.biggest_discount(items)
    pass


if __name__ == '__main__':
    # track program execution time
    start_ts = time.time()
    print(f'launch time: {time.strftime("%I:%M %p")}')
    load_dotenv()   # load environment variables from .env file
    main()
    print(f'execution time: {time.time() - start_ts}')
