# Q1.Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})


d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3={}
sum=0
for x in d1:
    if x in d2:
        sum=d1[x]+d2[x]
        d1[x]=sum
        d2.pop(x)
d1.update(d2)
print(d1)


                                              
dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
sum=0
for x in dic1:
    if x in dic2:
        sum=dic1[x]+dic2[x]
        dic1[x]=sum
        dic2.pop(x)
dic1.update(dic2)
dic3.update(dic1)
print(dic3)





