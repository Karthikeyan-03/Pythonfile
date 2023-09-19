# no return type without arugument function in python
"""""
a = int(input("enter the a value:"))
b = int(input("enter the b value:"))
c = a + b
print("total", c)


# no return type of with arugument

def sub(a, b):
    c = a - b
    print("differince:", c)


sub(67, 98)
# return type without arugument in python

def mul():
    a=int(input("enter the a value:"))
    b=int(input("enter the b value:"))
    c=a*b
    return c

x=mul()
print("mul",x)
"""


# return type with arugument in python

def div(a, b):
    c = a / b
    return c


x = div(25, 2)
print("division", x)


# arbitary arugument in python

def loss(*win):


    print(win)

loss("ram,san,den,man")
