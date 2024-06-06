from app.repositories.cart_repository import CartRepository
from app.use_cases.cart import Cart
from app.entities.product import Product

if __name__ == "__main__":
    cartRepository = CartRepository()
    cart = Cart(cartRepository)
    product1 = Product(name="Item A", price=50)
    product2 = Product(name="Item B", price=30)
    cart.addProduct(product1)
    cart.addProduct(product2)
    total = cartRepository.getTotal()
    print(f"El precio total en el carrito es: ${total:.2f}")