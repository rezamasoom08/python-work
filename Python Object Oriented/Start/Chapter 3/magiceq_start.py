class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __eq__(self, value):
        if not isinstance(value,Book):
            raise ValueError("Can't compare book to a non-book")
        return (self.title == value.title and
                self.author == value.author and
                self.price == value.price)

    def __ge__(self, value):
        if not isinstance(value,Book):
            raise ValueError("Can't compare book to a non-book")
        return self.price >= value.price
    
    def __lt__(self, value):
        if not isinstance(value,Book):
            raise ValueError("Can't compare book to a non-book")
        return self.price < value.price


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("Marvel", "Max", 20.0)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)

print(b1 == b3)
print(b1 == b2)
#print(b1 == 42)

print(b2 >= b1)
print(b2 < b1)

books = [b1,b3,b2]
books.sort()
print([book.title for book in books])