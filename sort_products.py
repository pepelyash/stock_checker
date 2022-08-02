import json


def read_product_ids(path: str):
    with open(path, mode='r', encoding='utf-8') as f:
        data = json.loads(f.read())
    return data


def read_product_ids_price(path: str):
    with open(path, mode='r', encoding='utf-8') as f:
        data = json.loads(f.read())
    return data


def save_json(sorted_by_totalprice_desc: list):
    with open('saved.txt', mode='w', encoding='utf-8') as f:
        f.write(json.dumps(sorted_by_totalprice_desc))


def sortby_totalprice_desc(products_list):
    return sorted(products_list, key=lambda product: product['totalprice'], reverse=True)


def main(product_ids, products_price):
    # path1 = 'product_ids.txt'
    # path2 = 'products_price.txt'
    # product_ids = read_product_ids(path1)
    # products_price = read_product_ids(path2)['products']
    products_list = []
    for item in product_ids:
        item_count = product_ids[item]['quantity']
        if item in products_price:
            item_name = products_price[item]['name']
            item_price = products_price[item]['price']
            new_item = {
                'id': item,
                'name': item_name,
                'count': item_count,
                'price': item_price,
                'totalprice': int(item_price*item_count/100)
            }
            products_list.append(new_item)
    save_json(products_list)
    return products_list


if __name__ == '__main__':
    main()
