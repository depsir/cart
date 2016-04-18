from cart import Cart
from item import Item

basic_tax = 0.1
basic_tax_exclude = ['book', 'food', 'medical']

import_tax = 0.05


cart1 = Cart(basic_tax, import_tax, basic_tax_exclude)
cart1.add_item(Item(False, 'book', 'book', 12.49))
cart1.add_item(Item(False, 'stuff', 'music CD', 14.99))
cart1.add_item(Item(False, 'food', 'chocolate bar', 0.85))
cart1.print_receipt()
print

cart2 = Cart(basic_tax, import_tax, basic_tax_exclude)
cart2.add_item(Item(True, 'food', 'box of chocolates', 10.00))
cart2.add_item(Item(True, 'stuff', 'bottle of perfume', 47.50))
cart2.print_receipt()
print

cart3 = Cart(basic_tax, import_tax, basic_tax_exclude)
cart3.add_item(Item(True, 'stuff', 'bottle of perfume', 27.99))
cart3.add_item(Item(False, 'stuff', 'bottle of perfume', 18.99))
cart3.add_item(Item(False, 'medical', 'packet of headache pills', 9.75))
cart3.add_item(Item(True, 'food', 'box of chocolates', 11.25))
cart3.print_receipt()
print
