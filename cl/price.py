class Price23Vat:
    def __init__(self, pretax):
        self._pretax = pretax
        self._net = pretax / 1.23
        self._tax = pretax - self._net

    def get_net(self):
        return self._net

    def get_tax(self):
        return self._tax

    def get_pretax(self):
        return self._pretax

    def set_pretax(self, value):
        self._pretax = value
        self._net = value / 1.23
        self._tax = value - self._net

    def set_net(self, value):
        self._net = value
        self._pretax = value * 1.23
        self._tax = self._pretax - value

    def set_tax(self, value):
        self._tax = value
        self._net = self._tax / 0.23
        self._pretax = self._net + value



price = Price23Vat(123)
print(price.get_tax())
print(price.get_pretax())
print(price.get_net())
price.set_net(150)
print(price.get_tax())
print(price.get_pretax())
print(price.get_net())
price.set_pretax(200)
print(price.get_tax())
print(price.get_pretax())
print(price.get_net())
price.set_tax(23)
print(price.get_tax())
print(price.get_pretax())
print(price.get_net())
