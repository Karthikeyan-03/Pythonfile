class P1:
    def m1(self):
        print("parent 1 class")
class P2:
    def m2(self):
        print("parent 2 class")
class C(P1,P2):
    def m3(self):
        print("child method")

c=C()
c.m1()
c.m2()
c.m3()

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
