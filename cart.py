import math


class Cart(object):
    """Simple cart object

    This module provides a simple tax computing algorithm
    and the receipt layout print.

    A Cart is configured with two tax values:
    - basic_tax: a decimal value that represents tax percent
        applied to all goods unles they are exempt.
    - import tax: a decimal value that represents tax percent
        applied to imported goods

    An additional list of categories is used to manage exempt goods.

    Taxes are applied one at a time on the base price.
    Every tax amount is rounded up to the neares 0.05

    The receipt output is formatted in this way:
    one line for each cart item showing amount, if it is imported,
    the product name and the price after taxes.
    Two lines are added at the end of the receipt showing the total tax amount
    and the total price after taxes
    """
    def __init__(self, basic_tax, import_tax, basic_tax_exclude):
        super(Cart, self).__init__()

        self.items = []

        self.basic_tax = basic_tax
        self.basic_tax_exclude = basic_tax_exclude
        self.import_tax = import_tax

    def add_item(self, item):
        """Add an item to the cart

        item must be an object with these attributes:
        - name
        - price
        - category
        - imported
        """
        self.items.append(item)

    def round_to_up05(self, val):
        """Round a value up to the nearest 0.05

        Examples:
        round_to_up05(7.49) -> 7.50
        round_to_up05(7.41) -> 7.45
        """
        return math.ceil(val * 100 / 5) * 5 / 100

    def calc_tax_for_item(self, item):
        """Compute tax for the given item

        Taxes are computed according to the rules
        described in the module documentation.

        Returns the total tax amount as a decimal value
        """
        tax_amount = 0
        if item.imported:
            tax_amount += self.round_to_up05(item.price * self.import_tax)

        if item.category not in self.basic_tax_exclude:
            tax_amount += self.round_to_up05(item.price * self.basic_tax)

        return tax_amount

    def build_receipt(self):
        """Build the receipt

        Returns a string with the receipt layout.
        Lines are separated with newline character.

        The receipt follows this layout:
        for each item in the cart one line with amount, if it is imported,
        the product name and the price after taxes.
        Examples:
            Output 3:
            1 imported bottle of perfume: 32.19
            1 bottle of perfume: 20.89
            1 packet of headache pills: 9.75

        Two lines are added at the end of the receipt
        showing the total tax amount
        and the total price after taxes
        Example:
            Sales Taxes: 6.70
            Total: 74.68
        """
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
        receipt_lines.append('Total: %.2f' % total)
        return '\n'.join(receipt_lines)

    def print_receipt(self):
        """Print receipt to standard output"""
        print self.build_receipt()
