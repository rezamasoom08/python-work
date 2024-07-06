class Book:
    def __init__(self, title):
        self.title = title

class Newspaper():
    def __init__(self, name):
        self.name = name

# create some instance of the classes

b1 = Book("Marvel")
b2 = Book("Transformers")
n1 = Newspaper("India Today")
n2 = Newspaper("TOI")

# use type() to inspect the object type

print(type(b1))
print(type(n1))

# compare 2 types together

print(type(b1) == type(b2))

# use instance to compare a specific instance to a known type

print(isinstance(b1, Book))
print(isinstance(b1, Newspaper))
print(isinstance(n1, Newspaper))
print(isinstance(n1, object))