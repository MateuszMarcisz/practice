class Product:
    next_id = 1

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id = Product.next_id
        Product.next_id += 1


class ShoppingCart:
    def __init__(self):
        self.products = {}
        self.quantities = {}

    def add_product(self, product):
        if product.id in self.products:
            self.quantities[product.id] += 1
        else:
            self.products[product.id] = product
            self.quantities[product.id] = 1

    def remove_product(self, product):
        if product.id in self.products:
            self.quantities[product.id] -= 1
            if self.quantities[product.id] == 0:
                del self.products[product.id]
                del self.quantities[product.id]
        else:
            return "can't remove product that was not there"

    def change_product_quantity(self, product, new_quantity):
        if new_quantity == 0:
            del self.products[product.id]
            del self.quantities[product.id]
        if new_quantity < 0:
            raise ValueError('Product quantity cannot be negative')
        if product.id in self.products:
            self.quantities[product.id] = new_quantity
        if product.id not in self.products:
            pass

    def get_receipt(self):
        receipt = ''
        for product_id, quantity in self.quantities.items():
            product = self.products[product_id]
            total_price = product.price * quantity
            receipt += f"{product.name} - amount: {quantity}, price: {product.price:.2f}zł, total: {total_price:.2f}zł\n"
        return receipt


bread = Product('Bread', 2.70)
ham = Product('Ham', 8.40)
cheese = Product('Cheese', 4.40)
chive = Product('Chive', 1.50)
pepper = Product('Pepper', 2.35)
print(bread.name)
print(bread.id)
print(ham.id)
print(cheese.id)
print(pepper.price)
cart = ShoppingCart()
print(cart.products)
print(cart.quantities)
cart.add_product(ham)
cart.add_product(cheese)
cart.add_product(cheese)
cart.add_product(cheese)
cart.add_product(chive)
print(cart.products)
print(cart.quantities)
print(cart.get_receipt())
cart.remove_product(ham)
cart.remove_product(cheese)
print(cart.get_receipt())
