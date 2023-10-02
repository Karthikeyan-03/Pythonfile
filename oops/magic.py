class Book:
    def __init__(self,pages):
       self.pages=pages

    def __add__(self, other):
       return self.pages+other.pages

b1=Book(100)
b2=Book(200)
print(b1+b2)

class Assesment:
    def __init__(self,mark):
        self.mark=mark

    def __add__(self, other):
        return self.mark+other.mark

b1=Assesment(500)
b2=Assesment(300)
print(b1+b2)

