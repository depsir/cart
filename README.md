# Cart

Simple shopping cart.

This module provides a simple tax computing algorithm and the receipt layout print.

## Installation

To install this module simply clone the repository

```
git clone git@github.com:depsir/cart.git 
```

## Basic usage
```
# Import the module
import cart

# Build a cart
my_cart = cart.Cart(basic_tax=0.1,
                    import_tax=0.05,
                    basic_tax_exclude=['book', 'food', 'medical'])
# Add Items to cart
new_item = cart.Item(imported=False,
                     category='book',
                     name='book',
                     price=12.49)
my_cart.add_item(new_item)

# Print the receipt
my_cart.print_receipt()
```
This will output
```
1 book: 12.49
Sales Taxes: 0.00
Total: 12.49
```
## Test
To run the tests use
```
python -m unittest discover
```
# Exercise notes
This module is meant to solve the sales taxes problem.

The three example inputs provided in the problem explanation, are tested in a unit test.