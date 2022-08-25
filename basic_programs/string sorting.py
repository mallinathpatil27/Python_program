#accept the string and sort according to the alphabetical order

lst = [i for i  in input('enter string:').split(',')]


lst1=[]
for i in lst:
    lst1.append(i.strip())

lst1.sort()
print(lst1)
