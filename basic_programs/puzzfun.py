lst=[4, 5, 17, 9, 14, 108, -9, 12, 76,-102]

sum=0
ls=[]
for i in lst:
    if abs(i) >100:
        ls.append(i)
        print(i)
        

print(sum(lst))

