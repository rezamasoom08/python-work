from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float    

    def bookinfo(self):
        return f"{self.title} by {self.author}"

b1 = Book("War and Peace", "Leo Tolstoy", 200, 39.95)
b2 = Book("Marvel", "Max", 100, 20.0)

print(b1.title)
print(b1.author)

print(b1)
print(b1 == b2)

b1.title = "Cricket"
b1.pages = 500
print(b1.bookinfo())