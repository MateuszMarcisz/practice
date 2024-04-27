class Cart:
    def __init__(self):
        self.products = []

    def add(self, price, product_name):
        if isinstance(price, (int, float)) and isinstance(product_name, str):
            self.products.append((price, product_name))

    def summary(self):
        return self.products


class Discount20PercentCart(Cart):

    def summary(self):
        return [(price * 0.8, product_name) for (price, product_name) in self.products]


class Above3ProductsCheapestFreeCart(Cart):

    def summary(self):
        if len(self.products) < 3:
            return self.products
        else:
            discount = sorted(self.products)
            discount[0] = (0, discount[0][1])
            return discount


c1 = Cart()
c1.add(price=100, product_name='Ford')
print(c1.summary())
c2 = Discount20PercentCart()
c2.add(price=100, product_name='Ford')
print(c2.summary())
c3 = Above3ProductsCheapestFreeCart()
c3.add(price=300, product_name='Ford')
c3.add(price=200, product_name='Toyota')
c3.add(price=350, product_name='Lexus')
c3.add(price=500, product_name='Lamborghini')
print(c3.summary())
