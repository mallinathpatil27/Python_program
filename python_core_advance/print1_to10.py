'''
#factorial number
# num=int(input("enter a  number : "))
num=5
if num <0:
    print("enter positive number")
elif num ==0:
    print("zero factorial is 1")
else:
    facto=1
    for i in range(1,num+1):
        facto=facto*i
    print(facto)
# factorial number
# num=int(input("enter a  number : "))
num=5
fact=1
if num>0 and num ==0:
    print("enter the valid number :")
else:
    for i in range(1,num+1):
        fact=fact*i
print(fact)

# prime number
# num=int(input("enter a  number : "))
num=2
if num==0:
    print('Can not be checked for Prime Numbers')
elif num==1:
    print('Can not be checked for Prime Numbers')
else:
    for i in range(2,(num//2)+1):
        if num%i==0:
            print(num,'is not a Prime Number')
            break
    else:
        print(num,'is a Prime Number')

# armstrong number
def armstrong(n):
    s=str(n)
    sum=0
    for i in s:
        sum=sum+int(i)**3
    if sum == n:
        print("armstrong number")
    else:
        print("not a armstrong number")

armstrong(123)

# fibbonocci number
n=10
l=[0,1]
for i in range(n-2):
    next=l[i]+l[i+1]
    l.append(next)
print(l)


# anagram
st1=input('enter a string :')
st2=input('enter another string :')
s1=st1.strip()
s2=st2.strip()

if sorted(s1)==sorted(s2):
    print('its a anagram string')
else:
    print('not a anagram string')

# pallindrom
s=input("enter a string to check pallindrom :")
s2=s[::-1]
if s==s2:
    print("its a pallindrom ")
else:
    print('its not pallindrom')


str='my name is prafull'
st1=str.split(' ')
lst=[]
for i in st1:
    lst.append(i[::-1])
output=' '.join(lst)
print(output)

str='Aditya'
lst=[]
for i in str:
    if str.index(i) % 2 ==0:
        i1=i.upper()
    else:
        i1=i.lower()
    lst.append(i1)
print("".join(lst))

str="a5b3d2x5"
output=''

for i in str:
    if i.isalpha():
        output=output+i
        previous=i
    else:
        output=output+previous*(int(i)-1)
print(output)

#
str="a8z46dg3"
alpha=[]
num=[]
for i in str:
    if i.isalpha():
        alpha.append(i)
    else:
        num.append(i)
res=sorted(alpha)+sorted(num)
print(''.join(res))

lst=[1,3,2,3,4,5,6,6,6,6,7,7,7,8,8,8]
res=[]
res1=[]
for i in lst:
    if i not in res:
        res.append(i)
    else:
        res1.append(i)
print(res)
print(set(res1))

lst1=list(range(1,4))
lst=['a','b','c']
res=[]
for i in lst:
    for j in lst1:
        res.append(i+str(j))

print(res)

str="the cat and the dog are fighting"
lst=str.split()
dic={}
for i in lst:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
for k,v in dic.items():
    print(k,"-->",v)
print(dic)


lst=[1,3,2,3,4,5,6,6,7,7,7,8,8,8,5]
for i in lst:
    if i%2 != 0:
        print(i,lst.index(i),lst.count(i))

str='geeksforgeeks'
lst=[]
for i in str:
    lst.append(i)
for x in lst:
    print(x,lst.count(i))


#start triangle
rows=5
for i in range(1,rows+1):
    print("*"*i)
# print()

#reveres right triangle
n=5
for i in range(n):
    for j in range(1,n-1):
        print(" ",end=" ")
    for k in range(0,i+1):
        print("*",end=" ")
    print()


for i in range(0,5):
    for j in range(0,5):
        print("*",end=" ")
    print()


n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end =" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()

n=5
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(2*(n-i)-1):
        print("*",end=" ")
    print()

#
# n=5
# i=n
# while i>1:
#     print(" "*(n-1)+"*"*i)
#     i-=1

def decor(fun):
    def inner():
        x=fun()
        return x+2
    return inner
@decor
def fun():
    return 10

# out=decor(fun)
# print("the number is ",out())
# print(fun())

def smart(fun):
    def inner(a,b):
        print("divid the numbers",a,b)
        if b == 0:
            print("divid not possible")
            return
        else:
            return fun(a,b)
    return inner

@smart
def div(a,b):
    return a/b

result=div(10,0)
print(result)

def double(fun):
    def inner(a,b):
        x=a*2
        y=b*2
        return x+y
    return inner

@double
def num(a,b):
    return a+b

out=num(10,5)
print("the sum of the number is ",out)

def double(fun):
    def inner(a,b):
        if a % 2==0 or b%2==0:
            return a*a+b*b
        else:
            return a+b
    return inner
@double
def num(a,b):
    return a+b
out=num(2,4)
print("the sum of the number is ",out)
# decorator
def double(fun):
    def inner(a):
        return a*2
    return inner

@double
def num(a):
    return a
out=num(2)
print("the sum of the number is ",out)

'''
#time analysis








