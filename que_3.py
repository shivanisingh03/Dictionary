# Question 3
# Ek program likhiye jo ki dictionaries ki values ka sum print kare. 

def returnSum(myDict):
    sum = 0
    for i in myDict:
        sum = sum + myDict[i]
    return sum
dict = {
        'data1':100,
        'data2': -54,
        'data3': 247
       } 
print("Sum :", returnSum(dict))








stock= {
        'data1':100,
        'data2': -54,
        'data3': 247
       } 
total = 0
for i in stock.values():
    total += i
print(total)


