user=int(input("enter your number "))
i=0
list=[]
while i<user:
    name=input("enter name ")
    age=int(input("enter the age "))
    i+=1
    c={}
    c[name]=age
    list.append(c)
print(list)
