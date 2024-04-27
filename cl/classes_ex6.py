class Price:
    def __init__(self, value):
        self.value = round(float(value), 2)

    def from_usd(self):
        self.value = self.value * 3.8
        return Price(self.value)

    def from_eur(self):
        self.value = self.value * 4.5
        return Price(self.value)

    def __str__(self):
        return f'{self.value} PLN'


złotówki = Price(100)
print(złotówki)
dolary = Price(100).from_usd()
print(dolary)
