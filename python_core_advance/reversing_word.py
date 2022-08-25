#reversing the string with word

s=input('ente the string:')
l=s.split()
lst=[]

i=len(l)-1

while i>=0:
    lst.append(l[i])
    i=i-1

output=' '.join(lst)
print(output)

