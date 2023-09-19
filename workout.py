# def decor (func):
#     def inner(name):
#         if name=="jana":
#             print("hi very good morning you got a job,you are good in python programming")
#         else:
#             func(name)
#     return inner
# @decor
# def wish(name):
#     print("hello",name,"goodmrng")
# wish("ram")
# wish("jana")
# wish("gopal")

# def mygen():
#     yield 'a'
#     yield 'b'
# g=mygen()
# for i in g:
#     print(i)
# print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))

# def fib():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# for f in fib():
#     if f>=1000:
#         break
#     print(f)

# square = {x : x*x for x in range(1,6)}
# print(square)
# doubles={x : 2*x for x in range(1,6)}
# print(doubles)

# d={}
# m=0
# s=""
# while True:
#     print("Enter 1 to continue or 0 to exit")
#     a=int(input(","))
#     if(a==1):
#         s=input("Enter the name")
#         m=int(input("Enter the mark"))
#         d[s]=m
#         continue
#     else:
#         break
#
# print("Enter a name to get the mark")
# g=(input(","))
# g1=d[g]
# print(g1)

# def sum(*args):
#     variable = 0
#     for a in args:
#         variable = variable + a
#
#     return variable
# print(sum(10,20))
# print(sum(10,20,30))
# print(sum(10,20,30,40))

# def key(name,msg):
#     print("hi",name,msg)
# key(name="karthi",msg="goodmorning")

# def key(*n, **data):
#     print(n)
#     print(data)
#     for x in n:
#         print(x)
#         for a,b in data.items():
#             print(a,b)
# key('karthi','dharshan',age=20,city='salem')



