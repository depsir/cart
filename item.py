class Item(object):
    """Represent a sellable item of the catalog"""
    def __init__(self, imported, category, name, price):
        super(Item, self).__init__()
        self.imported = imported
        self.category = category
        self.name = name
        self.price = price
