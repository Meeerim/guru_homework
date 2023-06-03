"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(100) is True
        assert product.check_quantity(999) is True
        assert product.check_quantity(1001) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(0)
        assert product.quantity == 1000
        product.buy(100)
        assert product.quantity == 900

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(product.quantity + 1)


@pytest.fixture()
def cart():
    return Cart()


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, cart, product):
        cart.add_product(product, 10)
        assert cart.products == {product: 10}
        cart.add_product(product, 10)
        assert cart.products == {product: 20}

    def test_remove_product(self, cart, product):
        cart.add_product(product, 15)
        cart.remove_product(product, 15)
        assert cart.products[product] == 0
        cart.add_product(product, 10)
        cart.remove_product(product, 15)
        assert cart.products == {}
        cart.add_product(product, 4)
        cart.remove_product(product, 2)
        assert cart.products[product] == 2

    def test_clear_product(self, cart, product):
        cart.add_product(product)
        cart.clear()
        assert len(cart.products) == 0

    def test_buy_product(self, cart, product):
        cart.add_product(product, 10)
        cart.buy()
        assert cart.products == {}
        assert product.quantity == 990

    def test_buy_with_error(self, cart, product):
        cart.add_product(product, 1010)
        with pytest.raises(ValueError):
            cart.buy()
