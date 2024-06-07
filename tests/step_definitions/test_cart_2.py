from app.entities.product import Product
from app.repositories.cart_repository import CartRepository
from app.use_cases.cart import Cart
from pytest_bdd import scenarios, scenario, given, when, then, parsers
import pytest

@scenario('../features/test_cart.feature', 'Add product with price greater than $100')
def testAdd():
    pass

@pytest.fixture
@given("a cart")
def cart():
    cartRepository = CartRepository()
    return Cart(cartRepository)

@when(parsers.parse("I add a product with a price of {price:d}"))
def addProduct(cart, price):
    cart.addProduct(Product(name="Product 1", price=price))

@then(parsers.parse("the total should be {total:d}"))
def checkTotal(cart, total):
    assert cart.calculateTotal() == total