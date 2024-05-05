class Square:
    def __init__(self, side):
        self._side = side
        self._perimeter = 4 * self._side
        self._area = self._side ** 2
        self._diagonal = self._side * 2 ** 0.5

    @property
    def side(self):
        return self.get_side()

    @property
    def area(self):
        return self.get_area()

    @property
    def perimeter(self):
        return self.get_perimeter()

    @property
    def diagonal(self):
        return self.get_diagonal()

    def get_side(self):
        return self._side

    def get_area(self):
        return self._area

    def get_perimeter(self):
        return self._perimeter

    def get_diagonal(self):
        return self._diagonal

    def set_side(self, new_length):
        self._side = new_length
        self._perimeter = 4 * self._side
        self._area = self._side ** 2
        self._diagonal = self._side * 2 ** 0.5

    def set_perimeter(self, new_length):
        self._perimeter = new_length
        self._side = new_length / 4
        self._area = self._side ** 2
        self._diagonal = self._side * 2 ** 0.5

    def set_area(self, new_area):
        self._area = new_area
        self._side = new_area ** 0.5
        self._perimeter = 4 * self._side
        self._diagonal = self._side * 2 ** 0.5

    def set_diagonal(self, new_length):
        self._diagonal = new_length
        self._side = new_length / 2 ** 0.5
        self._perimeter = 4 * self._side
        self._area = self._side ** 2

    @side.setter
    def side(self, new_side):
        self.set_side(new_side)

    @perimeter.setter
    def perimeter(self, new_perimeter):
        self.set_perimeter(new_perimeter)

    @area.setter
    def area(self, new_area):
        self.set_area(new_area)

    @diagonal.setter
    def diagonal(self, new_diagonal):
        self.set_diagonal(new_diagonal)


sq = Square(11)
print(sq.get_side())
print(sq.side)
print(sq.get_area())
print(sq.area)
print(sq.get_perimeter())
print(sq.perimeter)
print(sq.get_diagonal())
sq.perimeter = 20
print(sq.get_side())
print(sq.get_area())
print(sq.get_perimeter())
print(sq.get_diagonal())
