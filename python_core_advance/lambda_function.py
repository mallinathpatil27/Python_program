#lambda functions exampls
'''Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that
multiplies argument x with argument y and print the result'''

f=lambda x: x+15
print(f(5))

#Write a Python program to sort a list of dictionaries using Lambda.
models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]

k=sorted(models,key=lambda x: x['make'])
print(list(k))

#Write a Python program to filter a list of integers using Lambda.
nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

object=list(filter(lambda x: x%2 ==0,nums))
print(object)
from functools import *
sum=reduce(lambda x,y: x+y,object)
print(sum)

#Write a Python program to find whether a given string starts with a given character using Lambda

object=lambda x : True if x.startswith('P') else False
print(object('Palli'))

#Write a Python program to extract year, month, date and time using Lambda
import datetime
now=datetime.datetime.now()
print(now)
year=lambda x: x.year
month=lambda x:x.month
day=lambda x:x.day
#t=lambda x:x.time()
print(year(now))
print(month(now))
print(day(now))
#print(t(now))

#Write a Python program to check whether a given string is number or not using Lambda.

is_num=lambda q:q.isdigit()
print(is_num('3a45'))

#Write a Python program to create Fibonacci series upto n using Lambda.

from functools import *

fab_series=lambda n:reduce(lambda x,_:x+[x[-1]+x[-2]],range(n-2),[0,1])

print(fab_series(10))

fab=lambda n :reduce(lambda x,_:x+[x[-1]+x[-2]],range(n-2),[0,1])
print(fab(20))

#Write a Python program to find the values of length six in a given list using Lambda.

WEEK=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

day=filter(lambda x: x if len(x)==6 else '',WEEK)
print(list(day))

#pallindrom

t= ["php", "w3r", "Python", "abcd", "Java", "aaa"]

object=filter(lambda x: x[::] ==x[::-1],t)
print(list(object))

#numbers sorted from string

str1="sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"

str_num=[i for i in str1.split(' ')]
number=sorted(int(x) for x in str_num if x.isdigit())

for i in ((filter(lambda x: x>len(str_num),number))):
    print(i,end=' ')

print(str_num)
print(number)

#Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using lambda function.

nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]

even=list(filter(lambda num:num %2 ==0,nums))
print((even))

#Write a Python program to find the list with maximum and minimum length using lambda.

def max_length(in_list):
    max_len=max(len(x) for x in in_list)
    max_list=max(in_list,key=lambda i:len(i))
    return(max_len,max_list)

t1=max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])
print(t1)

#Write a Python program to sort each sublist of strings in a given list of lists using lambda.

def sort(lst):
    obj=[sorted(x,key=lambda x: x[0]) for x in lst]
    return obj
t=sort([["green", "orange"], ["black", "white"], ["white", "black", "orange"]])
print(t)

#Write a Python program to sort a given list of lists by length and value using lambda.

def sort1(lst):
    result=sorted(lst,key=lambda l:(len(l),l)) # it will filter the len from l
    return result

t=sort1([[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]])
print(t)

#Write a Python program to find the maximum value in a given heterogeneous list using lambda.
def max_val(nums):
    max_val=max(nums,key=lambda i: (isinstance(i,int),i))
    return (max_val)
t1=max_val(['Python', 3, 2, 4, 5, 'version'])
print(t1)

#Write a Python program to count float number in a given mixed list using lambda.

def count(list1):
    n=list(map(lambda i:isinstance(i,float),list1))
    result=len([e for e in n if e])
    return result

t2=count([1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22])
print(t2)

#Write a Python program to find index position and value of the maximum and minimum values in a given list of numbers using lambda.
lst=[12,33,23,10.11,67,89,45,66.7,23,12,11,10.25,54]
m=lst.index(max(lst))
print(m)

#LAMBDA FUNCTION WITH IF WITHOUT ELSE .
square = lambda x: x*x if(x>0) else None
print(square(6))

#List = [expression(i) for i in another_list if filter(i)]
lst  =  [x ** 2  for x in range (1, 11)   if  x % 2 == 1]
print(lst)