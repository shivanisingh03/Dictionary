# Question 1
# a = {(1,2):1,(2,3):2}
# print(a[1,2]) 


# Question 2
# b= {"a":1,"b":2,"c":3}
# print (b["a","b"]) 


# # Question 3
# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
# addone('Apple')
# addone('Banana')
# addone('apple')
# addone('Apple')
# print (len(fruit))
# print(fruit) 


# # Question 4
# Student = {}
# Age = {}
# Details = {}
# Student['name'] = "bikki"
# Age['student_age'] = 14
# Details['Student'] = Student
# Details['Age'] = Age
# print (len(Details["Student"]))
# print(Student) 
# print(Age)
# print(Details)
# print(Student)
 

# # Question 5
# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]

# print (sum)
# print(my_dict) 


# # Question 6
# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates['box']))
# print(crates) 


# # Question 7
# rec = {
# "Name" : "Python", 
# "Age":"20",
# "Addr" : "NJ", 
# "Country" :"USA"
# }
# id1 = id(rec)
# del rec
# rec = {
#     "Name" : "Python", 
#     "Age":"20", 
#     "Addr" : "NJ", 
#     "Country" : "USA"
#     }
# id2 = id(rec)
# print(id1 == id2)


 







name=int(input("enter your name limit "))
i=0
b=[]
c=[]
s=[]
while i<=name:
    name1=input("enter the names ")
    age1=int(input("enter the age "))
    b.append(name1)
    c.append(age1)
    j=0
    while j<len(b):
        s.append({[b[i],c[i]]})
        j+=1
    i+=1
    a={}
    a.update(s)
print(a)












