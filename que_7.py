# Question 7
# Ek list lijiye aur uske andar dictionaries me keys and values likhiye jaisa ki 
# niche dikhaya gaya hai (Sample Data) aur uske baad saare unique values ko ek list
#  me print karaye. 
d=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
] 
a=[]
for i in d:
     for j in i:
          if i[j] not in a:
               a.append(i[j])
print(a) 


