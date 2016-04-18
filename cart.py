import math


class Cart(object):
    """Simple cart object"""
    def __init__(self):
        super(Cart, self).__init__()

        self.items = []


    def apply_taxes(self):
        pass
    def add_item(self, item):
        self.items.append(item)

    def print_receipt(self):
        # 1 book: 12.49
        # 1 music CD: 16.49
        # 1 chocolate bar: 0.85
        # Sales Taxes: 1.50
        # Total: 29.83
        pass

    def checkout(self):
        pass
