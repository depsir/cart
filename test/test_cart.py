import unittest
from cart import Cart
from item import Item


class TestWithBasicCart(unittest.TestCase):

    def get_basic_cart(self):
        basic_tax = 0.1
        basic_tax_exclude = ['book', 'food', 'medical']
        import_tax = 0.05

        return Cart(basic_tax, import_tax, basic_tax_exclude)


class TestCartExampleInputs(TestWithBasicCart):

    def setUp(self):
        self.cart1 = self.get_basic_cart()
        self.cart1.add_item(Item('book', 12.49, 'book', False))
        self.cart1.add_item(Item('music CD', 14.99, 'stuff', False))
        self.cart1.add_item(Item('chocolate bar', 0.85, 'food', False))

        self.cart2 = self.get_basic_cart()
        self.cart2.add_item(Item('box of chocolates', 10.00, 'food', True))
        self.cart2.add_item(Item('bottle of perfume', 47.50, 'stuff', True))

        self.cart3 = self.get_basic_cart()
        self.cart3.add_item(Item('bottle of perfume', 27.99, 'stuff', True))
        self.cart3.add_item(Item('bottle of perfume', 18.99, 'stuff', False))
        self.cart3.add_item(Item('packet of headache pills', 9.75, 'medical', False))
        self.cart3.add_item(Item('box of chocolates', 11.25, 'food', True))

    def test_output_1(self):
        expected_result = """1 book: 12.49
1 music CD: 16.49
1 chocolate bar: 0.85
Sales Taxes: 1.50
Total: 29.83"""
        self.assertEqual(self.cart1.build_receipt(), expected_result)

    def test_output_2(self):
        expected_result = """1 imported box of chocolates: 10.50
1 imported bottle of perfume: 54.65
Sales Taxes: 7.65
Total: 65.15"""
        self.assertEqual(self.cart2.build_receipt(), expected_result)

    def test_output_3(self):
        expected_result = """1 imported bottle of perfume: 32.19
1 bottle of perfume: 20.89
1 packet of headache pills: 9.75
1 imported box of chocolates: 11.85
Sales Taxes: 6.70
Total: 74.68"""
        self.assertEqual(self.cart3.build_receipt(), expected_result)


class TestRound_up_to_05(TestWithBasicCart):
    def setUp(self):
        self.cart = self.get_basic_cart()

    def test_integer_value(self):
        self.assertEqual(self.cart.round_up_to_05(12), 12)

    def test_already_rounded_value(self):
        self.assertEqual(self.cart.round_up_to_05(7.45), 7.45)

    def test_ceil_not_round_value(self):
        self.assertEqual(self.cart.round_up_to_05(7.49), 7.50)

    def test_ceil_not_floor_not_round_value(self):
        self.assertEqual(self.cart.round_up_to_05(7.41), 7.45)

if __name__ == '__main__':
    unittest.main()
