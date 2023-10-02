class P:
    def property(self):
        print("Gold+Land+Cash")

    def marry(self):
        print("Arrange Marriage")

class C(P):
    def marry(self):
        super().marry()
        print("Love Marriage")

c=C()
c.marry()
c.property()