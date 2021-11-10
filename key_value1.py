name=int(input("enter your name limit "))
i=0
b=[]
c=[]
s=[]
while i<=name:
    name1=input("enter the names ")
    age1=int(input("enter the age "))
    b.append(name1)
    c.append(age1)
    j=0
    while j<len(b):
        s.append([b[i],c[i]])
        j+=1
    i+=1
    a={}
    a.update(s)
print(a)



            




