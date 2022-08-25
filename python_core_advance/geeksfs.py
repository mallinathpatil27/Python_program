#important functions

#dictonary
#items
#SLICE
#update =is used to update the dict d1.update(d2)
#get functions=d.get=get(key,def_value) functions
#setdefault functions .
#ord(),hex(),oct()
##ord convert into ASCI Charector values
#any=any operator return true if any of the operator true its like any
#all =return true if all the items are true its like and
#trued=returns floating point division.d.truediv(a,b)
#floordiv(a,b)
#lt(a,b),le(a,b)= it is less than or less than or equal to functions
#settitem(object,position,values)=is used to assign the values at perticular position to change the values

#delitem(object,position)= is used to delete at perticular values
#getitem(object,position)=it is acces perticular value
#list.CONCATE(S1,S2) AND list.CONTAINES(s1,s2)
#before that we import random module
#random module=lst.randint(0,5)=print random integer number
# if we want print random floating values
#random.random()
#random values from list we use choice(list) functions
#module datetime import datetime
#datetime.date.today()= without time
#datetime.datetime.now() it will print date along with time
#import re
#compile ('[a-e]')
# import itertools
# print(list(itertools.product('ABC','12'))) #product operator
# # [('A', '1'), ('A', '2'), ('B', '1'), ('B', '2'), ('C', '1'), ('C', '2')]
# print(list(itertools.permutations('ABC',2)))
# # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
# print(list(itertools.combinations('ABC',2)))
#
# import calendar
# print(calendar.monthrange(2022,7))
#
# import operator
# x='avd'
# y="dataengineer"
# z=operator.iconcat(x,y)
# print(z)
# #finding the duplicate charecter in a string
# str="geeksforgeeks"
# dup={}
# for char in str:
#     if char in dup:
#         dup[char]+=1
#     else:
#         dup[char]=1
# print(dup)
#
#
# for key,value in dup.items():
#     if value >1:
#         print(key,end=" ")
# print()
#
# result=max(dup,key=dup.get)
# print(result)

lst = [15, 16, 17, 10, 12, 20, 10, 28, 10]
l=[]
for i in lst:
    sum=0
    for x in str(i):
        sum=sum+int(x)
    l.append(sum)
print(l)

ls=[12, 67, 98, 34]
re=[]
for i in ls:
    sum=0
    for ele in str(i):
        sum=sum+int(ele)
    re.append(sum)
print(re)




















































