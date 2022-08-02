import time
from dotenv import load_dotenv
import shop_api
import workout_products_list


def main():
    product_ids, products_price = shop_api.main()
    print(product_ids, products_price)
    products_list = workout_products_list.get_products_list(product_ids, products_price)
    workout_products_list.sortby_totalprice_desc(products_list)
    pass


if __name__ == '__main__':
    # track program execution time
    start_ts = time.time()
    print(f'launch time: {time.strftime("%I:%M %p")}')
    load_dotenv()   # load environment variables from .env file
    main()
    print(f'execution time: {time.time() - start_ts}')
