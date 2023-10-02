class P1:
    def m1(self):
        print("parent 1 class")
class P2:
    def m2(self):
        print("parent 2 class")

class P3:
    def m3(self):
        print("Parent 3 class")

class C(P1,P2,P3):
    def m4(self):
        print("child method")

    def m5(self):
        print("child class 2")


c=C()

c.m1()
c.m2()
c.m3()
c.m4()
c.m5()
#mro method resolution order
# class P1:
#     def m1(self):
#         print("parent 1")
# class P2:
#     def m1(self):
#         print("parent 2")
# class C(P1,P2):
#     def m2(self):
#         print("child method")
#
# c=C()
# c.m1()
# c.m2()
#
