# class Student:
#     school="python class"
#     def __init__(self, m1, m2, m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#     def avg(self):
#         return (self.m1+self.m2+self.m3)/3
#     @classmethod
#     def getschool(cls):
#         return cls.school
#     @staticmethod
#     def info():
#         print("this is python class for you")
# jana=Student(40,90,70)
# dharshan=Student(100,20,40)
# print(jana.avg())
# print(dharshan.avg())
# print(Student.getschool())
# print(Student.info())

# class Area:
#     count=0
#     def __init__(self,areaname,personname,houseno):
#         self.areaname=areaname
#         self.personname=personname
#         self.houseno=houseno
#         Area.count+=1

# import time
# class Test:
#     def __init__(self):
#         print("constructor executive")
#     def __del__(self):
#         print("fullfill my last wish and perform cleanup")
# list=[Test(),Test(),Test()]
# del list
# time.sleep(5)
# print("end of application")

#inheritance
# class Vehicle:
#     def __init__(self,mileage,cost):
#         self.mileage=mileage
#         self.cost=cost
#     def show_details(self):
#         print("i am vechicle")
#         print("mileage of vehicle is",self.mileage)
#         print("cost of vehicle is",self.cost)
# v1=Vehicle(500,500)
# v1.show_details()

#destructor
# import time
# class Test:
#     def __init__(self):
#         print("object initilalize")
#     def __init__(self):
#         print("database connection close")
# t1=Test()
# t1=None
# time.sleep(5)
# print("end of application")

#constructor in count method
# class Test:
#     count=0
#     def __init__(self):
#         Test.count=Test.count+1
#
#     @classmethod
#     def noofobject(cls):
#         print("no of object created:",cls.count)
# t1=Test()
# t2=Test()
# Test.noofobject()
# t3=Test()

#has/a relationship[compostion method]
# class Engine:
#     a=10
#     def __init__(self):
#         self.b=20
#     def m1(self):
#         print("engine specifiction")

# class Car:
#     def __init__(self):
#         self.engine=Engine()
#     def m2(self):
#         print("car using engine class function")
#         print(self.engine.a)
#         print(self.engine.b)
#         self.engine.m1()
# c=Car()
# c.m2()

# class College:
#     a="BSC"
#     def _init_(self):
#         self.b="SURESH"
#     def m1(self):
#         print("MUTHAYAMMAL MEMORIAL COLLEGE")
# class Dep:
#     def _init_(self):
#         self.College = College()
#     def m2(self):
#         print("MUTHAYAMMAL MEMORIAL COLLEGE:")
#         print("department:",self.College.a)
#         print("HOD NAME:",self.College.b)
#         self.College.m1()
# c = Dep()
# c.m2()

n=int(input("Enter no of student:"))
d={}
for i in range(n):
    name = input("Enter student name:")
    marks = int(input("Enter student marks:"))
    d[name] = marks

while True:
    name = input("Enter student name to get marks:")
    marks = d.get(name,-1)
    if marks == -1:
        print("student not found:")
    else:
        print("Marks of",name,"are",marks)

    option = input("Do you want to find another student mark[yes/no]:")
    if option == "no":
        print("Thanks for using our application")
        break



