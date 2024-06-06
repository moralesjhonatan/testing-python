import pytest
from app.entities.product import Product
from app.repositories.cart_repository import CartRepository
from app.use_cases.cart import Cart

def testAddProduct():
    cartRepository = CartRepository()
    cart = Cart(cartRepository)
    product = Product(name="Item A", price=50)
    cart.addProduct(product)
    assert cartRepository.getTotal() == 50

def testAddProductWithNegativePrice():
    cartRepository = CartRepository()
    cart = Cart(cartRepository)
    product = Product(name="Item B", price=-10)
    with pytest.raises(ValueError):
        cart.addProduct(product)