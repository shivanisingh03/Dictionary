# output:-{"a":[],"b":[],"c":[]}

dict={"a":[1,2,3],"b":[4,5,6],"c":[7,8,9]}
for i in dict:
    if type(dict[i])==list:
        dict[i]=[]
print(dict)




        
                






















