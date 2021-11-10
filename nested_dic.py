dict1={'a':1,'b':2,'c':{'d':3,'e':4,'f':{'g':5,'h':6}}}
sum=0
for i in dict1:
    # print(dict1[i])
    if type(dict1[i])==dict: 
        for j in dict1[i]:
            if type(dict1[i][j])==dict:
                for c in dict1[i][j]:
                    sum+=dict1[i][j][c]
            else:
                sum=sum+dict1[i][j]
    else:
        sum=sum+dict1[i]
print(sum)

