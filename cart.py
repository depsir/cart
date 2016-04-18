import math


class Cart(object):
    """Simple cart object"""
    def __init__(self, basic_tax, import_tax, basic_tax_exclude):
        super(Cart, self).__init__()

        self.items = []

        self.basic_tax = basic_tax
        self.basic_tax_exclude = basic_tax_exclude
        self.import_tax = import_tax

    def add_item(self, item):
        self.items.append(item)

    def round_to_up05(self, val):
        return math.ceil(val*100/5)*5/100

    def calc_tax_for_item(self, item):
        price = item.price
        import_tax_amount = 0
        basic_tax_amount = 0

        if item.imported:
            import_tax_amount = self.round_to_up05(price * self.import_tax)

        if item.category not in self.basic_tax_exclude:
            basic_tax_amount = self.round_to_up05(price * self.basic_tax)
        tax_amount = import_tax_amount + basic_tax_amount

        return tax_amount

    def build_receipt(self):
        # 1 book: 12.49
        # 1 music CD: 16.49
        # 1 chocolate bar: 0.85
        # Sales Taxes: 1.50
        # Total: 29.83
        receipt_lines = []
        tax_total = 0
        total = 0
        for item in self.items:
            tax = self.calc_tax_for_item(item)
            item_total_price = tax + item.price
            receipt_lines.append(
                '1 %s%s: %.2f' % ('imported ' if item.imported else '',
                                  item.name,
                                  item_total_price))
            tax_total += tax
            total += item_total_price
        receipt_lines.append('Sales Taxes: %.2f' % tax_total)
        receipt_lines.append('Total: %.2f' % total )
        return '\n'.join(receipt_lines)

    def print_receipt(self):
        print self.build_receipt()
