from abc import *
class Fruit(ABC):
    @abstractmethod
    def taste(self):
        pass
f=Fruit()

from abc import *
class Vehicle(ABC):
    @abstractmethod
    def wheels(self):
        pass

class Bus(Vehicle):
    pass
b=Bus()

from abc import *
class Vehicle(ABC):
    @abstractmethod
    def noofwheels(self):
        pass

class Bus(Vehicle):
    def noofwheels(self):
        return 7

class Auto(Vehicle):
    def noofwheels(self):
        return 4

b=Bus()
c=Auto()
print(b.noofwheels())
print(c.noofwheels())