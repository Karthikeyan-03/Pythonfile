class Instagram:
    def m1(self):
        print("Instagram most user in india")

class Reels:
    def m2(self):
        print("Highest views growup to make content creator")

class C(Instagram,Reels):
    def m3(self):
        print("Create an account or log in to Instagram "
              "A simple, fun & creative way to capture,"
              "edit & share photos, videos & messages with friends & family")

c=C()
c.m1()
c.m2()
c.m3()