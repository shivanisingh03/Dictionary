


d={"first":1,"second":2,"third":3,"fourth":4,"fifth":5,"sixth":6}
a=[]
b=[]
c=[]
for i in d.values():
    if i not in a:
        a.append(i)
        for j in d.keys():
            if j not in b:
                b.append(j)
for x in range(0,len(a)):
    c.append([a[x],b[x]])
d1={}
d1.update(c)
print(d1)