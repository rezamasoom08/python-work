# Using class-level and static methods

class Book:

    # Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER","PAPERBACK","EBOOK")

    # double-underscore properties are hidden from other classes
    __booklist = None

    # create a class method
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES
    
    # create a static method
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist
    
    # instance methods receive a specific object instance as an argument and operate on data specific to that object instance

    def set_title(self, newtitle):
        self.title = newtitle
    
    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype

# access the class attribute
print("Book types:", Book.get_book_types())

# create some book instances
b1 = Book("Title1", "HARDCOVER")
#b2 = Book("Title", "COMIC")

thebooks = Book.getbooklist()
thebooks.append(b1)
#thebooks.append(b2)
print(thebooks)