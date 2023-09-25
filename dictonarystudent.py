n=int(input("Enter No Of Student:"))
d={}
for i in range(n):
    name = input("Enter Student Name:")
    marks = int(input("Enter Student Marks:"))
    d[name] = marks

while True:
    name = input("Enter Student Name To Get Marks:")
    marks = d.get(name,-1)
    if marks == -1:
        print("Student Not Found:")
    else:
        print("Marks of",name,"are",marks)

    option = input("Do You Want To Find Another Student Mark[yes/no]:")
    if option == "no":
        print("Thanks For Using Our Application")
        break