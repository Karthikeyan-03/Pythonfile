class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eatndrink(self):
        print("eat briyani and drink")
class Employee(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
    def work(self):
        print("coding python")
    def empinfo(self):
        print("emp name:",self.name)
        print("emp age:",self.age)
        print("emp no:",self.eno)
        print("emp sal:",self.esal)

e=Employee("darshan",22,80,80000)
e.eatndrink()
e.work()
e.empinfo()

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno=rollno
        self.marks=marks
    def __str__(self):
        return"name={},age={},rollno={},marks={}".format(self.name,self.age,self.rollno,self.marks)

s1= Student("ram",80,90,100)
print(s1)

has a relationship method
class Engine:
    a=10
    def __init__(self):
        self.b=20
    def m1(self):
        print("engine specifiction")

class Bike:
    def __init__(self):
        self.engine=Engine()
    def m2(self):
        print("bike using petrol")
        print(self.engine.a)
        print(self.engine.b)
        self.engine.m1()
c=Bike()
c.m2()

def generator():
    yield "H"
    yield "E"
    yield "L"
    yield "L"
    yield "O"

test=generator()
for i in test:
    print(i)

def even_numbers(n):
    for x in range(n):
       if (x%2==0):
           yield x
num = even_numbers(20)
for i in num:
    print(i)

def test(n):
    return n*n
def getSquare(n):
    for i in range(n):
        yield test(i)

sq = getSquare(10)
for i in sq:
    print(i)