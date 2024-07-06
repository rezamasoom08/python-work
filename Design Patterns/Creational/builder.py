class Director():
    def __init__(self, builder):
        self._builder = builder
    
    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tyres()
        self._builder.add_engine()
            
    def get_car(self):
        return self._builder.car

class Builder():
    def __init__(self):
        self.car = None
    
    def create_new_car(self):
        self.car = Car()

class SkyLarkBuilder(Builder):
    def add_model(self):
        self.car.model = "Skylark"
    
    def add_tyres(self):
        self.car.tyres = "Regular"
    
    def add_engine(self):
        self.car.engine = "Turbo Engine"

class Car():
    def __init__(self):
        self.model = None
        self.tyres = None
        self.engine = None
    
    def __str__(self):
        return '{} | {} | {}'.format(self.model, self.tyres, self.engine)

builder = SkyLarkBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()

print(car)