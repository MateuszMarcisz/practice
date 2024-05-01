class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        if self.check_isbn(isbn):
            self.isbn = isbn
        else:
            raise ValueError("Invalid ISBN")

    @staticmethod
    def check_isbn(isbn_number):
        isbn_number = str(isbn_number).replace('-', '')
        return isbn_number.isdigit() and (len(isbn_number) == 10 or len(isbn_number) == 13)


book = Book("Lord of the Strings", "JRR Torvaldskien", 9780007136575)
print(book.isbn)
