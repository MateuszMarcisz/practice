class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def describe(self):
        print(f" x: {self.x}, y: {self.y}, color: {self.color}")

    def distance(self, x, y):
        return ((self.x - x)**2 + (self.y - y)**2)**0.5

    def __str__(self):
        return f"figura koloru {self.color} o środku w punkcie({self.x}, {self.y})"



cokolwiek = Shape(50, 50, "red")
cokolwiek.describe()
print(cokolwiek.distance(x = 10, y = 10))
print(cokolwiek.__str__())
