# Question 9
# "MISSISSIPPI" iss word me har letter ki occurrency count karke ek dictionary me 
# store karaye. Jisme letter dictionary ki keys aur occurrency Uss dictionary ki 
# values hongi.


str="w3resource"
b={}
i=0
for i in str:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)











