class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher

class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        #self.title = title
        self.author = author
        #self.price = price
        self.pages = pages

class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)
        #self.title = title
        #self.author = publisher
        #self.price = price
        #self.pages = period

class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)
        #self.title = title
        #self.author = publisher
        #self.price = price
        #self.pages = period

b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("My Times", "TOI", 6.0, "Daily")
m1 = Magazine("Science Fiction", "Springer Nature", 5.99, "Monthly")

print(b1.author)
print(n1.publisher)
print(b1.price, n1.price, m1.price)