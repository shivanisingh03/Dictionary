d={"first":"1", "second": "2", "third": "3", "four": "4", "five":"5", "six":"6","seven":"7"}
a=[]
b=[]
s=[]
for x in d.values():
    if x not in a:
        a.append(x)
        for y in d.keys():
            if y not in b:
                b.append(y)
for i in range(0,len(a)):
    s.append([a[i],b[i]])

c={}
c.update(s)
print(c)