import unittest
from cart import Cart
from item import Item


class TestWithBasicCart(unittest.TestCase):

    def get_basic_cart(self):
        basic_tax = 0.1
        basic_tax_exclude = ['book', 'food', 'medical']
        import_tax = 0.05

        return Cart(basic_tax, import_tax, basic_tax_exclude)


class TestCartInput1(TestWithBasicCart):

    def setUp(self):
        self.cart = self.get_basic_cart()
        self.cart.add_item(Item(False, 'book', 'book', 12.49))
        self.cart.add_item(Item(False, 'stuff', 'music CD', 14.99))
        self.cart.add_item(Item(False, 'food', 'chocolate bar', 0.85))

    def test_output_1(self):
        expected_result = """1 book: 12.49
1 music CD: 16.49
1 chocolate bar: 0.85
Sales Taxes: 1.50
Total: 29.83"""
        self.assertEqual(self.cart.build_receipt(), expected_result)


class TestCartInput2(TestWithBasicCart):

    def setUp(self):
        self.cart = self.get_basic_cart()
        self.cart.add_item(Item(True, 'food', 'box of chocolates', 10.00))
        self.cart.add_item(Item(True, 'stuff', 'bottle of perfume', 47.50))

    def test_output_2(self):
        expected_result = """1 imported box of chocolates: 10.50
1 imported bottle of perfume: 54.65
Sales Taxes: 7.65
Total: 65.15"""
        self.assertEqual(self.cart.build_receipt(), expected_result)


class TestCartInput3(TestWithBasicCart):

    def setUp(self):
        self.cart = self.get_basic_cart()
        self.cart.add_item(Item(True, 'stuff', 'bottle of perfume', 27.99))
        self.cart.add_item(Item(False, 'stuff', 'bottle of perfume', 18.99))
        self.cart.add_item(Item(False, 'medical', 'packet of headache pills', 9.75))
        self.cart.add_item(Item(True, 'food', 'box of chocolates', 11.25))

    def test_output_3(self):
        expected_result = """1 imported bottle of perfume: 32.19
1 bottle of perfume: 20.89
1 packet of headache pills: 9.75
1 imported box of chocolates: 11.85
Sales Taxes: 6.70
Total: 74.68"""
        self.assertEqual(self.cart.build_receipt(), expected_result)

if __name__ == '__main__':
    unittest.main()
