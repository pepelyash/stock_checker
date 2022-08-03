import json
import copy


def load_from_file():
    with open('sortedby/items_all.json', 'r', encoding='utf8') as file:
        return json.load(file)


def save_to_file(products):
    with open('sortedby/items_all.json', 'w', encoding='utf8') as file:
        json.dump(products, file, indent=4, ensure_ascii=False)


# functions for custom sorting
def keyfunc3(tup):
    key, products = tup
    return products['discount_percent']


def biggest_discount(products):
    # saved format is broken cuz of multiple copying
    items = copy.deepcopy(products)
    selection = {}

    for item in items:
        if not items[item]['quantity'] == 0 and items[item].get('oldPrice'):
            selection[item] = items[item]
            selection[item]['discount_percent'] = 100-int(items[item]['price']/items[item]['oldPrice']*100)

    res = sorted(selection.items(), key=keyfunc3, reverse=True)

    with open('sortedby/biggest_discount_desc.json', 'w', encoding='utf8') as file:
        json.dump(res, file, indent=4, ensure_ascii=False)


def keyfunc2(tup):
    key, products = tup
    return products['price']


def price_asc(products):
    # saved format is broken cuz of multiple copying
    items = copy.deepcopy(products)
    selection = {}

    for item in items:
        if not items[item]['quantity'] == 0:
            selection[item] = items[item]

    res = sorted(selection.items(), key=keyfunc2)

    with open('sortedby/price_asc.json', 'w', encoding='utf8') as file:
        json.dump(res, file, indent=4, ensure_ascii=False)


def keyfunc1(tup):
    key, products = tup
    return products['totalcost']


def totalcost_670to630_desc(products):
    # saved format is broken cuz of multiple copying
    items = copy.deepcopy(products)
    selection = {}

    for item in items:
        if 630 < items[item]['totalcost'] < 670 and items[item]['quantity'] < 10:
            selection[item] = items[item]

    res = sorted(selection.items(), key=keyfunc1, reverse=True)

    with open('sortedby/totalcost_670to630_desc.json', 'w', encoding='utf8') as file:
        json.dump(res, file, indent=4, ensure_ascii=False)


