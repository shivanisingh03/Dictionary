# Q2. Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

# str="w3resource"
# a={}
# for i in str:
#     a[i]=a.get(i,0)+1
# print(a)




str="w3resource"
b={}
i=0
for i in str:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)





