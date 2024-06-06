class Cart:

    def __init__(self, cartRepository):
        self.cartRepository = cartRepository

    def addProduct(self, product):
        if product.price < 0:
            raise ValueError("El precio del producto no puede ser negativo")
        self.cartRepository.addProduct(product)