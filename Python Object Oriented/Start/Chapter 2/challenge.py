from abc import ABC, abstractmethod

class Asset(ABC):
    def __init__(self, price):
        self.price = price
    
    @abstractmethod
    def get_description(self):
        pass

class Stock(Asset):
    def __init__(self, ticker, price, company):
        super().__init__(price)
        self.company = company
        self.ticker = ticker
    
    def get_description(self):
        return f"{self.ticker}: {self.company} -- ${self.price}"

class Bond(Asset):
    def __init__(self, price, description, duration, yieldamt):
        super().__init__(price)
        self.description = description
        self.duration = duration
        self.yieldamt = yieldamt
    
    def get_description(self):
        return f"{self.description}: {self.duration}yr : ${self.price} : {self.yieldamt}"