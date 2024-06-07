class CartRepository:

    def __init__(self):
        self.items = []

    def addProduct(self, product):
        self.items.append(product)

    def removeProduct(self, product):
        self.items.remove(product)

    def calculateTotal(self):
        total = sum(product.price for product in self.items)
        if total > 100:
            total = total - (total * 0.1)
        return total