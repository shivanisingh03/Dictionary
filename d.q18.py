# Q18.Write a Python program to get the maximum and minimum value in a dictionary.

numbers = {'a': 100, 'b': 200, "d":400, 'c':300}
j=0
for i in numbers:
    # print(numbers[i])
    if j<numbers[i]:
        j=numbers[i]
print(j)
    



