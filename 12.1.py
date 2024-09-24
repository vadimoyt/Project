class Product:
    def __init__(self, name, shop=None, price=None):
        self._name = name
        self._shop = shop
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def shop(self):
        return self._shop

    @property
    def price(self):
        return self._price

    def __str__(self):
        return f"Product: {self._name}, Shop: {self._shop}, Price: {self._price} RUB"

class Store:
    def __init__(self):
        self._products = []

    def add_product(self, product):
        if isinstance(product, Product):
            self._products.append(product)
        else:
            raise TypeError("Only instances of Product can be added")

    def remove_product(self, product):
        if product in self._products:
            self._products.remove(product)
        else:
            raise ValueError("Product not found in store")

    def list_products(self):
        return [str(product) for product in self._products]

    def find_product_by_name(self, name):
        for product in self._products:
            if product.name.lower() == name.lower():
                return product
        return 'Not found'

    def sort_products_by_price(self, descending=False):
        sorted_products = sorted(self._products, key=lambda p: p.price, reverse=descending)
        return [str(product) for product in sorted_products]

    def filter_products_by_name(self, filter_name):
        filtered_products = [product for product in self._products if filter_name.lower() in product.name.lower()]
        return [str(product) for product in filtered_products]

    def sum_prices(self, *products):
        total_price = 0
        for product in products:
            if product in self._products:
                total_price += product.price
            else:
                raise ValueError(f"Товар '{product.name}' не найден")
        return total_price

    def add_prices(self, x, y):
        if 0 <= x < len(self._products) and 0 <= y < len(self._products):
            x_product = self._products[x]
            y_product = self._products[y]
            return f"Сумма цены товара '{x_product.name}' и товара '{y_product.name}' равна {x_product.price + y_product.price} RUB"
        else:
            raise IndexError("Вышли за диапазон")

product1 = Product(name='Oven', shop='5 Element', price=1000)
product2 = Product(name='Microwave', shop='21 Vek', price=200)
product3 = Product(name='Sofa', shop='21 Vek', price=3930)

store = Store()
store.add_product(product1)
store.add_product(product2)
store.add_product(product3)

try:
    total_price = store.sum_prices(product1, product2)
    print(f"Total price of selected products: {total_price} RUB")
except ValueError as e:
    print(e)

try:
    sum_prices_message = store.add_prices(0, 1)
    print(sum_prices_message)
except (IndexError, ValueError) as e:
    print(e)

print(store.list_products())
print(store.find_product_by_name('Oven'))
print(store.sort_products_by_price())