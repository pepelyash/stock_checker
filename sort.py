import json


def keyfunc_price(tup):
    key, products = tup
    return products['price']


def price_asc(products):
    items = sorted(products.items(), key=keyfunc_price, reverse=True)

    with open('products_price_asc.json', 'w', encoding='utf8') as file:
        json.dump(items, file, indent=4)


def keyfunc_totalcost(tup):
    key, products = tup
    return products['totalcost']


def totalcost_desc(products):
    items = sorted(products.items(), key=keyfunc_totalcost, reverse=True)

    with open('sort_by_default.json', 'w', encoding='utf8') as file:
        json.dump(items, file, indent=4, ensure_ascii=False)


def main():
    # sorting by default
    with open('products_list.json', 'r', encoding='utf8') as file:
        products = json.load(file)

    price_asc(products)
    totalcost_desc(products)


if __name__ == '__main__':
    main()
