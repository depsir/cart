import math

basic_tax = 0.1
basic_tax_exclude = ['book', 'food', 'medical']

import_tax = 0.05


def round_to_up05(val):
    return math.ceil(val*100/5)*5/100


def calc_tax_for_item(item):
    price = item['price']
    import_tax_amount = 0
    basic_tax_amount = 0

    if item['imported']:
        import_tax_amount = round_to_up05(price * import_tax)

    if item['category'] not in basic_tax_exclude:
        basic_tax_amount = round_to_up05(price * basic_tax)
    tax_amount = import_tax_amount + basic_tax_amount

    return {'base_price': price,
            'import_tax_amount': import_tax_amount,
            'basic_tax_amount': basic_tax_amount,
            'tax_amount': tax_amount,
            'price_after_taxes': price + tax_amount
            }


def build_item(imported, category, name, price):
    return {'imported': imported,
            'category': category,
            'name': name,
            'price': price}

items = []
items.append(build_item(False, 'book', 'book', 12.49))
items.append(build_item(False, 'stuff', 'music CD', 14.99))
items.append(build_item(False, 'food', 'chocolate bar', 0.85))
items.append(build_item(True, 'food', 'box of chocolates', 10.00))
items.append(build_item(True, 'stuff', 'bottle of perfume', 47.50))
items.append(build_item(True, 'stuff', 'bottle of perfume', 27.99))
items.append(build_item(False, 'stuff', 'bottle of perfume', 18.99))
items.append(build_item(False, 'medical', 'packet of headache pills', 9.75))
items.append(build_item(True, 'food', 'chocolates', 11.25))

for item in items:
    print item['name']
    print calc_tax_for_item(item)
