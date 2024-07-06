from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(20, 40))    


@dataclass
class Book:
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    price: float = field(default_factory=price_func)  

    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, {self.pages} pages"

b1 = Book("War and Peace", "Leo Tolstoy", 200, 39.95)
b2 = Book("Marvel", "Max", 100, 20.0)

print(b1)
print(b2)
