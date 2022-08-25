# Deriving rectamgular class from square class
class Square:
    def __init__(self,x):
        self.x = x

    def area(self):
        print("area of square:",self.x * self.x)

class Rectangle(Square):
    def __init__(self,x,y):
        super().__init__(x)
        self.y = y
    def area(self):
        super().area()
        print('area of rectangular:',self.x * self.y)


r=Rectangle(11,14.5)
r.area()
m=Square(10)
m.area()
#
#

# #epoch
# import time
# ep =time.time()
# print(ep,'seconds')
#
# dt=time.ctime(ep)
# print(dt)

#to know the system data and time

from time import *

dt=ctime()
print(dt)

from datetime import *
dt = datetime.now()
print(dt)

dt =datetime.today()
print(dt)
#
# #to know the birthday
#
# d,m,y = [ int(i) for i in input('enter date(dd/mm/yyyy): ').split('/')]
#
# dt=date(y,m,d)
# str=dt.strftime("you were born %A  and it is %jth day in te year")
# print(str)

#working with duration

dt=datetime(2022, 4, 7, 8, 46, 38)
duration =timedelta(days=20,hours=10,minutes=48, seconds=31)
print("future date and time =",dt+duration)
print("future date and time =",dt-duration)

#sort a group of dates
n=int(input('how many dates? '))
print('enter dates : ')
lst=[]
for i in range(n):
    d,m,y =[int(x) for x in input('enter date (dd/mm/yyyy)').split('/')]
    dt = date(y,m,d)
    lst.append(dt)

lst.sort()
print('sorted dates:')
for i in lst:print(i)
