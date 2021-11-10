# Question 10
# Ek dictionary ki value ke sabhi items ko count kijiye jo ki ek list me hai.


Adict =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
count = 0
for i in Adict:
   if isinstance(Adict[i], list):
      count += len(Adict[i])
print(count)



# a_dictionary = {"a": 1, "b": 2,"c":3}
# dictionary_length = len(a_dictionary)
# print(dictionary_length)





