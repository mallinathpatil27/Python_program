# #date and time and regex
import time as time
dt=time.ctime()
print(dt)
#
# from time import *
# dt =ctime()
# print(dt)

from datetime import *
dt=datetime.now()
print(dt)
#
dt=datetime.today()
print(dt)
#
# d=date(2016, 4, 29)
# print(d)
# t=time(2,30)
# dt=datetime.combine(d,t)
# print(dt)
#

d1=datetime(2022,7,7)
period=timedelta(days=100)
print(d1+period)











#
# dt=datetime.now()
# str=dt.strftime('Date = %d , %B, %Y')
# print(str)
# str=dt.strftime('today is %A and this month is %B and this is th %j')
# print(str)
# str=dt.strftime('current time = %H:%M:%S')
# print(str)

#to know the day when birthday is given

# d,m,y=[int(i) for i in input('enter date(dd/mm/yyyy): ').split('/')]
#
# dt=date(y,m,d)
# str=dt.strftime("your born on %A and the your month is %B and day is %d")
# print(str)
#
# #working with duration
# dt=datetime(2022,4,5,7,56,56)
# duration=timedelta(days=20,hours=10,minutes=10)
# print('future date;',dt+duration)
#
# #sorting the group of dates
from datetime import *
# n=int(input("how many dates ?"))
# lst=[]
# for i in range(n):
#     d,m,y =[int(x) for x in input('enter dt (dd/mm/yyyy):').split('/')]
#     dt=date(y,m,d)
#     lst.append(dt)
# lst.sort()
# print('sorted dates:')
# for i in lst:print(i)
#
# # import calendar as cl
# #
# # cl=cl.isleap(2022)
# # print(cl)
#
# d1=datetime(2022,6,17)
# duration=timedelta(days=60 ,hours=24,minutes=60)
# print('newdate for placement drive is :', d1+duration)
#
# dt=datetime.now()
# # print('current time :{}/{}/{}'.format(dt.day,dt.month,dt.year))
# #
# # #then time taken by the program
# # from time import *
# # t1=perf_counter()
# #
# # for i in range(10):print(i,end=" ")
# # sleep(3)
# #
# # t2=perf_counter()
# #
# # print(t2-t1)
#
# #regular expressions
# # import re
# # str = 'Kumbhmela will be conducted at Ahmedabad in India.Ahmedabad is good city'
# # res=re.sub(r'Ahmedabad','Allahabad',str)
# # print(res)
# #
# # str1= 'anil akhil anant arun arati arundhati abhijit ankur'
# # result=re.findall(r'a[nk][\w]*',str1)
# # print(result)
# #
# # dt = 'Vijay 20 1-5-2001, Rohit 21 22-10-1990, Sita 22 15-09-2000'
# # result1=re.findall(r'\d{1,2}-\d{1,2}-\d{4}',dt)
# # print(result1)
# #
#
#
# import re
# str = 'man sun mop run manners mamshkseu machin'
# result = re.findall(r'm\w\w ', str)
# print(result)
#
#
# import re
# str = 'man sun mop run '
# result = re.findall(r'm?\w\w+', str)
# print(result)