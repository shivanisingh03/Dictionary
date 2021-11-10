a=["shivani"]
i=0
d={}
while i<len(a):
    j=0
    while j<len(a[i]):
        d.update({j:a[i][j]})
        j+=1
    i+=1
print(d)
