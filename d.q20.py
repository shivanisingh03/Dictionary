# Q20.Write a Python program to check a dictionary is empty or not.
# Write a Python program to combine two dictionary adding values for common keys. 
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

