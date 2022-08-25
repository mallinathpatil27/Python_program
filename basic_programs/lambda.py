#write a lambda to find a square of number

def square(x):
    return x*x

res = square(5)
print(res)

#convert the above into lambda

f = lambda x: x*x
print(f(5))


#write a lambda to find sum of two numbers

def sum(a,b):
    res =a+b
    return res

z=sum(10,11)
print('sum:',z)

f= lambda x,y: x+y
print('the lambda sum is :',f(10,11))


#printing the 1 to 100

'''f= lambda x:x<10,print(i) 
print(f(1))
'''

#to test whether no is even or odd


def even_odd(n):
    if n%2==0:
        return 'even'
    else:
        return 'odd'

str=even_odd(5)
print(str)

#lambda functions

f = lambda n:'even' if n%2 ==0 else 'odd'
print(f(4))        


#lambda printing 1 to 10 values
f=[lambda x=x: x+1 for x in range(10)]

for f in f:
    print(f())


#filter even or odd or +ve or -ve
lst =[1,2,3,-1,-2,-6,7,-8,9]

obj=filter(lambda x: x<=0,lst)
print(list(obj))

#find the squares of elements in the list
lst =[1,2,3,-1,-2,-6,7,-8,9]

obj=map(lambda x: x*x,lst)
print(list(obj))

# to find product of all elements

#import functool
from functools import *
mytpl =(2,3,4,5,6)

res=reduce(lambda x,y:x*y,mytpl)
print(res)

