#removing the duplicate charector from the string
s=input('enter the string:')
ls=[]

for x in s:
    if x not in ls:
        ls.append(x)
output=''.join(ls)
print(output)
