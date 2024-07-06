class Book:
    def __init__(self, title, author, page, price):
        self.title = title
        self.author = author
        self.page = page
        self.price = price
        self.__secret = "This is a secret attribute"

    #create instance methods

    def getprice(self):
        if hasattr(self,"_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount

b1 = Book("Cricket","Sachin", 1000, 500)
b2 = Book("Marvel","Stanley",5000, 1000)

print(b1.getprice())
print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())

print(b2._Book__secret)
print(b2.__secret())