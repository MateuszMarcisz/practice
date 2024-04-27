class Price:
    def __init__(self, value):
        self.value = round(float(value), 2)

    @classmethod
    def from_usd(cls, value):
        return cls(value*3.8)

    @classmethod
    def from_eur(cls, value):
       return cls(value*4.5)

    def __str__(self):
        return f'{self.value} PLN'


złotówki = Price(100)
print(złotówki)
dolary = Price.from_usd(100)
print(dolary)
euro = Price.from_eur(100)
print(euro)
