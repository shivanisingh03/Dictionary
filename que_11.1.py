# Question 11
# Ek code likhiye jo dictionary ki 3 highest value print karaye.

from collections import Counter
my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
k = Counter(my_dict)
high = k.most_common(3) 
for i in high:
    print(i[1]," ")



my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
a=[]
for i in range(3):
    max=0
    for j in my_dict:
        if max<my_dict[j]:
            max=my_dict[j]
            b=j
    a.append(b)
    my_dict.pop(b)
print(a)







