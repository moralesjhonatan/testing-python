class CartRepository:

    def __init__(self):
        self.cart = []

    def addProduct(self, product):
        self.cart.append(product)

    def getTotal(self):
        return sum(product.price for product in self.cart)