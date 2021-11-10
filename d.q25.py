# Write a Python program to create a key-value list pairings in a given dictionary. 
# Original dictionary:
# {1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
# A key-value list pairings of the said dictionary:
# [{1: 'Jean Castro', 2: 'Lula Powell', 3: 'Brian Howell', 4: 'Lynne Foster', 5: 'Zachary Simon'}]


a={1: ['Jean Castro'], 2: ['Lula P owell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
b={}
c=[]
for i in a:
    for j in a[i]:
        if type(a[i])==list:
            b.update([{i,j}])
        else:
            b.update(i)
c.append(b)
print(c)





