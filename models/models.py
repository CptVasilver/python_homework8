class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        return self.quantity >= quantity
        # """
        # TODO Верните True если количество продукта больше или равно запрашиваемому
        #     и False в обратном случае
        # """
        # raise NotImplementedError

    def buy(self, quantity):
        if not self.check_quantity(quantity):
            raise ValueError
        else:
            self.quantity -= quantity
            return True
        # """
        # TODO реализуйте метод покупки
        #     Проверьте количество продукта используя метод check_quantity
        #     Если продуктов не хватает, то выбросите исключение ValueError
        # """
        # raise NotImplementedError

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        # if self.products == {}:
        #     self.products = dict[product, buy_count]
        if self.products.get(product):
            self.products.update({product: (buy_count + self.products.get(product))})
        else:
            self.products.update({product: buy_count})
        # """
        # Метод добавления продукта в корзину.
        # Если продукт уже есть в корзине, то увеличиваем количество
        # """
        # raise NotImplementedError

    def remove_product(self, product: Product, remove_count=None):
        if remove_count is None or remove_count >= self.products.get(product):
            del self.products[product]
        else:
            self.products.update({product: (self.products.get(product) - remove_count)})

        # """
        # Метод удаления продукта из корзины.
        # Если remove_count не передан, то удаляется вся позиция
        # Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        # """
        # raise NotImplementedError

    def clear(self):
        self.products.clear()

    def get_total_price(self) -> float:
        total = 0
        for product, count in self.products.items():
            total += product.price * count
        return total

    def buy(self):
        # """
        # Метод покупки.
        # Учтите, что товаров может не хватать на складе.
        # В этом случае нужно выбросить исключение ValueError
        # """
        # raise NotImplementedError
        if len(self.products) == 0: return False

        success = True
        for product, count in self.products.items():
            success &= product.buy(count)
        self.products.clear()
        return success
