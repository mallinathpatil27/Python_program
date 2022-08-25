#program to print even number from 1 to 10
i=0
while i <= 10:
    print(i)
    i=i+2

# to check the number wheather it is even or odd
def armstr(n):
    s=str(n)
    sum=0
    for i in range(len(s)):
        sum=sum+int(s[i])**3
    return sum==int(n)

s=armstr(153)
print(s)

# another way to find the armstrong numbers
n=int(input("enter a number"))
s=str(n)
sum=0
for i in s:
    sum=sum+int(i)**3
print(sum)
if sum == n:
    print("it is armstrong")
else:
    print("it is not armstrong")

# fabinoci series
n=10
l=[0,1]
for i in range(n-2):
    next=l[i]+l[i+1]
    l.append(next)
print(l)

# reversing the string
str="my name is mallinath"
s1=str.split()
l=[]
for i in s1:
    l.append(i[::-1])

out=' '.join(l)
print(out)

lst=str[::-1].split(" ")
print(lst)
fi=' '.join(lst)
print(fi)
o=''.join(reversed(str))
print(o)

# string operations
str="Aditya"
lst=[]
for i in str:
    if str.index(i) %2 ==0:
        i1 = i.upper()
    else:
        i1=i.lower()
    lst.append(i1)
print(''.join(lst))

# expanding the string
# output:aaaaabbbccdd
str="a5b3c2d2"
output=''
for i in str:
    if i.isalpha():
        output=output+i
        pre=i
    else:
        output=output+pre*(int(i)-1)
print(output)

st="a5b3c2d2"
output=''
for i in st:
    if i.isalpha():
        output=output+i
        pre=i
    else:
        output=output + pre *(int(i)-1)
print(output)

# sorting the charector and string separately
# output:abcehhnst6788
s="a8bc6het78snh"
char=[]
num=[]
for i in s:
    if i.isalpha():
        char.append(i)
    else:
        num.append(i)

output=sorted(char)+sorted(num)
print(''.join(output))

# finding the number of occurance
# output:{3: 3, 4: 3, 5: 1, 6: 1, 7: 1, 8: 2, 9: 3, 1: 3, 2: 1}
lst=[3,4,5,6,7,8,8,9,9,9,1,1,1,2,3,4,4,3]
dup={}
count=0
for i in lst:
    if i in dup:
        dup[i]+=1
    else:
        dup[i]=1
print(dup)






