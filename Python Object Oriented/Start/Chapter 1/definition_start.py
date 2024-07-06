#create a basic class

class Book:

    def __init__(self, title):
        self.title = title

#create instance of the class
book1 = Book("Brave new world")
book2 = Book("war and peace")

#print the class and property
print(book1)
print(book2.title)