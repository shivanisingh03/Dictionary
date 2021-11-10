list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,] 
k=[]
i=0
while i<len(list1):
    k.append([list1[i],list2[i]])
    i+=1
l={}
l.update(k)
print(l)