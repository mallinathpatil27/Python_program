# #REGULAR EXPRESSION
#
# str = 'man sun moo run mat'
# import re
# obj=re.search(r'm\w\w',str)
#
# if obj:
#     print(obj.group())
# else:
#     print('not found')

import re

# str='malli 20 1-5-2001,mahesh 20 12-10-2002,rahul 23 15-09-2001 ,avd 23 22-1-2233'
# lst=re.findall(r'\d{1,2}-\d{1,2}-\d{4}',str)
# for date in lst:
#     print(date)
# print(lst)
#
# lst =re.findall(r' \d\d ',str)
# print(lst)

# a regex to extract names starting with 'an' or 'ak'

# str=' anil akhil  anant arun arathi arundhathi abhijit ankur anikesh adith anukl'
# lst=re.findall(r'a[nk]\w*',str)
# print(lst)

#regexp to split the string where number  is found
#
# import re
#
# str='anil 2222 akhil 9999 anant 98979 abhijit 1234 ankur 6789 anikesh 1543 adith 1 anukl'
#
# lst=re.findall(r'[a-zA-Z]+',str)
# print(lst)
#
# lst=re.split(r'\d+',str)
# print(lst)

#
# f=open("malli.txt","w")
# a= f.write("mallinath is king of univers\n")
# print(a)
# f.close()

#
# f=open("malli.txt","a")
# a= f.write("mallinath is king of univers\n")
# print(a)
# f.close()
#
# # handle read and write both
# f =open("malli.txt","r+")
# print(f.read())
# f.write("thank you avd \n")
# print(f.read())

# with open ('malli.txt') as f:
#     a = f.readlines()
#     print(a)
#
# f =open("malli.txt","r+")
# print(f.readlines())
# print(f.read())
# f.close()

#
# f=open("D:/malli.txt",'r+')
# print(f.readlines())
# f.close()
# print(f.read())
# f.write("thank you avd \n")
# print(f.read())

















