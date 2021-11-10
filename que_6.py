dic1={
    "ball":"red",
    "bat":4,
    "wickets":8,
    "ball":"green",
    "bat":3
    } 
s={}
for i in dic1:
    s.update({i:dic1[i]})
print(s)