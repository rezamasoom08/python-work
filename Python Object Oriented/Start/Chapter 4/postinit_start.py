from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float    

    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, {self.pages} pages"

b1 = Book("War and Peace", "Leo Tolstoy", 200, 39.95)
b2 = Book("Marvel", "Max", 100, 20.0)

print(b1.description)
print(b2.description)
