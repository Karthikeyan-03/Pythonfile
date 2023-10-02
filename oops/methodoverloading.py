class Test:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("sum",a+b+c)
        elif a!=None and b!=None:
            print("sum",a+b)
        else:
            print("Please Provide 2 or 3 argument")

t=Test()
t.sum()
t.sum(10,20)
t.sum(10,20,30)

