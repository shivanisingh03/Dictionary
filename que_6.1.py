# Question 6
# Ek program likhiye jo dictionary me se duplicate keys hata de
dic={
    "ball":"red",
    "bat":4,
    "wickets":8,
    "ball":"green",
    "bat":3
    } 
result = {}
for key,value in dic.items():
    if value not in result.values():
        result[key] = value
print(result)










