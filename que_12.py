# Question 12
# Ek program likhiye jo:- Ek dictionary me 1 se 15 tak saare numbers ki keys 
# banaye aur unke square unn keys ki values ho. 

b={}
for i in range(1,16):
    s=i*i
    b.update({i:s})
print(b)
