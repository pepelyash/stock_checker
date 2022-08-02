import time
import shop_api
import sort_products


def main():
    product_ids, products_price = shop_api.main()
    print(product_ids, products_price)
    products_list = sort_products.main(product_ids, products_price)
    sort_products.sortby_totalprice_desc(products_list)
    pass


if __name__ == '__main__':
    # track program execution time
    start_ts = time.time()
    print(f'launch time: {time.strftime("%I:%M %p")}')
    main()
    print(f'execution time: {time.time() - start_ts}')
