import json


def read_products_id(path: str):
    with open(path, mode='r', encoding='utf-8') as f:
        data = json.loads(f.read())
    return data


def read_products_id_price(path: str):
    with open(path, mode='r', encoding='utf-8') as f:
        data = json.loads(f.read())
    return data


def save_json(sorted_by_totalprice_desc: list):
    with open('saved.txt', mode='w', encoding='utf-8') as f:
        f.write(json.dumps(sorted_by_totalprice_desc))


def main():
    path1 = 'products_id.txt'
    path2 = 'products_price.txt'
    products_id = read_products_id(path1)
    products_price = read_products_id(path2)['products']
    products_list = []
    for item in products_id:
        item_count = products_id[item]['quantity']
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
    sorted_by_totalprice_desc = sorted(products_list, key=lambda product: product['totalprice'], reverse=True)
    save_json(sorted_by_totalprice_desc)
    pass


if __name__ == '__main__':
    main()
