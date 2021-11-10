dict={"p":[{"age":500},{"age":80},{"age":55},{"age":20}]}
for i in dict:
    max=0
    for j in dict[i]:
        for c in j:
            # min=(j[c])
            print(j[c]) 
            if (j[c])>max:
                max=j[c]
            if (j[c]<min):
                min=j[c]
    print(max)
    print(min)