#sorting the group of string
lst=[]

n=int(input('how many string:'))
for i in range(n):
    str=input('enter the strings:')
    lst.append(str)

lst.sort()

for i in lst:
    print(i,end='\t')