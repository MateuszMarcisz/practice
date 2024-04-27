class Book:
    def __init__(self, n, p, a):
        self.name = n
        self.price = p
        self.author = a

    def print_book_info(self):
        print(self.name)
        print(self.price)
        print(self.author)


class EBook(Book):
    def __init__(self, n, p, a, s):
        super().__init__(n, p, a)
        self.size_in_mb = s

    def print_book_info(self):
        super().print_book_info()
        print(self.size_in_mb)


b = EBook("Hobbit", 39.95,
          "J. R. R. Tolkien", 12)
b.print_book_info()
