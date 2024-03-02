"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart(product):
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(0)
        assert product.check_quantity(1000)
        assert not product.check_quantity(1001)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(1)
        assert product.buy(998)
        assert product.buy(1)
        assert product.buy(0)

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            assert product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_cart_add(self, cart, product):
        cart.add_product(product, 100)
        cart.add_product(product, 300)
        assert len(cart.products) == 1
        assert cart.products[product] == 400

    def test_cart_remove(self, cart, product):
        cart.add_product(product, 100)
        cart.remove_product(product, 100000000)
        assert len(cart.products) == 0

        cart.add_product(product, 100)
        cart.remove_product(product, 100)
        assert len(cart.products) == 0

        cart.add_product(product, 100)
        cart.remove_product(product, 99)
        assert cart.products[product] == 1

    def test_cart_clear(self, cart, product):
        cart.add_product(product, 100)
        cart.clear()
        assert not cart.products

    def test_cart_total(self, cart):
        product = [Product("book", 100, "This is a book", 1000),
                   Product("fruit", 103.4, "This is a fruit", 1000)]
        cart.add_product(product[0], 5)
        cart.add_product(product[1], 4)
        assert cart.get_total_price() == 913.6

    def test_cart_buy(self, cart):
        assert not cart.buy()
        product = [Product("book", 100, "This is a book", 1000),
                   Product("fruit", 100, "This is a fruit", 1000)]
        cart.add_product(product[0], 5)
        cart.add_product(product[1], 1000)
        assert cart.buy()
        cart.add_product(product[1], 1000)
        with pytest.raises(ValueError):
            assert cart.buy()

        # print()
