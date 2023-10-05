for i in "Apple":
    print(i)

for i in range(5):
    print(i)

for i in range(11):
    print(i)

for i in range(1,5):
    print(i)

#print 2 table using for loop?
for i in range(1,11):
    print(i,"x2=",i*2)

for i in range(1,11):
    print(i,"x3=",i*3)

#syntax
x=["Python","Programing","Tutorial"]
for i in x:
    print(i)

#print even number between 1 to 10?
for i in range(1,11):
    if(i%2==0):
        print(i)

#count the numbers of odd numbers between 1 to 10?
count=0
for i in range(1,11):
    if(i%2==0):
        count=count+1
print(count)

#count the number of odd and even numbers between 1 to 10?
oddcount=0
evencount=0
for i in range(1,11):
    if(i%2==0):
        oddcount=oddcount+1
    else:
        evencount=evencount+1
print(oddcount)
print(evencount)

#count the number which are divisible by 3and5(range 1-100)?
count=0
for i in range(1,101):
    if(i%3==0 and i%5==0):
        count=count+1
print(count)

