import pytest
from app.entities.product import Product
from app.repositories.cart_repository import CartRepository
from app.use_cases.cart import Cart

@pytest.fixture
def cart():
    cartRepository = CartRepository()
    return Cart(cartRepository)

def testAddProduct(cart):
    product = Product(name="Product 1", price=50)
    cart.addProduct(product)
    assert cart.calculateTotal() == 50
    #assert len(cart.cartRepository.items) == 1

def testRemoveProduct(cart):
    product = Product(name="Product 1", price=50)
    cart.addProduct(product)
    cart.removeProduct(product)
    assert len(cart.cartRepository.items) == 0

def testCalculateTotal(cart):
    cart.addProduct(Product(name="Product 1", price=50))
    cart.addProduct(Product(name="Product 2", price=40))
    assert cart.calculateTotal() == 90

def testAddProductWithNegativePrice(cart):
    product = Product(name="Product 3", price=-10)
    with pytest.raises(ValueError):
        cart.addProduct(product)