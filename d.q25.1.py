# Write a Python program to create a key-value list pairings in a given dictionary. 
# Original dictionary:
# {1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
# A key-value list pairings of the said dictionary:
# [{1: 'Jean Castro', 2: 'Lula Powell', 3: 'Brian Howell', 4: 'Lynne Foster', 5: 'Zachary Simon'}]


a={1: ['Jean Castro'], 2: ['Lula P owell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
c=[]
for i in a:
    a[i]=a[i][0]
# print(a)
c.append(a)
print(c)