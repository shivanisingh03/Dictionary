# Question 4
# Ek program likhiye jo ki nested dictionary me se first key or value ko remove 
# kare.
Dic= {
        1: 'NAVGURUKUL',
        2: 'IN',  
  	    3:{    
             'A' : 'WELCOME',
             'B' : 'To',
             'C' : 'DHARAMSALA'
            }
        }
del Dic[3]["A"]
print(Dic)