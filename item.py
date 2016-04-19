class Item(object):
    """Represent a sellable item of the catalog

    An item is described by:
    - name: A string that identifies this item
    - price: the shelf price before taxes
    - category: a string describing the item category
    - imported: a boolean which is true if this item is imported
    """
    def __init__(self, imported, category, name, price):
        super(Item, self).__init__()
        self.imported = imported
        self.category = category
        self.name = name
        self.price = price
