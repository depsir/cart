class Catalog(object):
    """Object that represents the product catalog"""
    def __init__(self):
        super(Catalog, self).__init__()
        self.products = {}

    def add(self, item):
        self.products[item.id] = item

    def get(self, id):
        return self.products[id]
