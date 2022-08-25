#this is student class
# from teacher import *
# class student:
#     def setid(self,id):
#         self.id =id
#     def getid(self):
#         return self.id
#     def setmarks(self,marks):
#         self.marks=marks
#
#     def getmarks(self):
#         return self.marks
#     def setaddress(self,addr):
#         self.addr=addr
#     def getadd(self):
#         return self.addr
#     def setname(self,name):
#         self.name=name
#     def getname(self):
#         return self.name
#
# s=student()
# s.setid(100)
# s.setname('malli')
# s.setmarks([12,23,45,67])
# s.setaddress('avd 1234 rths')
# print(s.getid(),s.getadd(),s.getname(),s.getmarks())
#
# class father:
#     def __init__(self):
#         self.pro=8000000
#     def display_pr(self):
#         print(self.pro)
# class son(father):
#     def __init__(self):
#         self.pro=200000
#     def display_pr(self):
#         print(self.pro)
# s=son()
# s.display_pr()

# class father:
#     def height(self):
#         print("hieght is 6.0 foot")
# class mother:
#     def color(self):
#         print('color is brown')
# class child(father,mother):
#     pass
#
# c=child()
# print('child inherited qualities:  ')
# c.height()
# c.color()


# class father:
#     def height(self):
#         print('height is 6.0 foot')
# class mother:
#     def color(self):
#         print('colore is brown')
# class child(father,mother):
#     pass
# c=child()
# c.height()
# c.color()

# method overloading

# class myclass:
#     def sum(self,a=0,b=0,c=0):
#         print('sum=',a+b+c)
# m=myclass()
# m.sum(10,15)
# m.sum(10,15,22.5)

#
#
# from abc import *
# class myclass(ABC):
#     @abstractmethod
#     def calculate(self,x):
#         pass #empty body, no code
# class sub1(myclass):
#     def calculate(self,x):
#         print('sqaure values = ', x*x)
# import math
# class sub2(myclass):
#     def calculate(self,x):
#         print('square root = ',math.sqrt(x))
#
# class sub3(myclass):
#     def calculate(self,x):
#         print('cube value',x**3)
#
# obj=sub1()
# obj.calculate(16)
# obj1=sub2()
# obj1.calculate(14)
# obj2=sub3()
# obj2.calculate(15)

# list practice
# ls=[12, 35, 9, 56, 24]
# ls1=[]
# lst2=[]
# for i in ls:
#     if i==ls[0]:
#         ls1.append(ls[0])
#     elif i==ls[-1]:
#         lst2.append(ls[-1])
#
# print(ls1,lst2)
# output=lst2+ls[1:-1]+ls1
# print(output)
#

# l=[]
# l.append(ls[-1])
# l.append(ls[1:-2])
# l.append(ls[0])
#
# print(ls)

# ls=[12, 35, 9, 56, 24]
# temp=ls[0]
# ls[0]=ls[-1]
# ls[-1]=temp
#
# print(ls)

#
# li = [23, 65, 19, 90]
# temp=li[1]
# li[1]=li[2]
# li[2]=temp
# print(li)

# lst = [ 1, 4, 5, 7, 8 ]
# count=0
# for i in lst:
#     count+=1
# print(count)
# print(len(lst))
#
# a=2
# b=4
# if a>b:
#     max=a
# else:max=b
# print(max)

# a=11
# b=12
# c=2
# if a>b and a>c:
#     max=a
# elif b>c:
#     max=b
# else:
#     max=c
# print(max)
#
# lst = [10, 11, 12, 13, 14, 15]
# ls=[]
# for i in range((len(lst)-1),0,-1):
#    ls.append(lst[i])
#
# print(ls)
# lst = [10, 11, 12, 13, 14, 15]
# ls1=[]
# ls1=lst[::-1]
# print(ls1)
#
# lst.reverse()
# print(lst)
lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]

print(lst.count(10))
x=10
print('{} has occured {} times'.format(x,lst.count(x)))

# l10= [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5]
# l=[4, 5, 1, 2, 9, 7, 10, 8]
# sum=0
# pro=1
# for i in l:
#     sum+=i
#     pro*=i
#
# print(sum)
# print(sum/len(l))
# print(pro)

# ls=[12, 67, 98, 34]
# re=[]
# for i in ls:
#     sum=0
#     for ele in str(i):
#         print(ele)
#         sum=sum+int(ele)
#     re.append(sum)
# print(re)
# lst=[1,2,3,5,6,7,7]
# pro=1
# for i in lst:
#     pro*=i
# print(pro)
# lst=[1,2,3,5,6,7,7]
# sum=[]
# prev=1
# for i in lst:
#     sum.append(prev*i)
#     prev=i
# print(sum)

# lst=[1,2,3,5,6,7,7]
# re=[]
# pre=0
# for i in lst:
#     res=pre+i
#     re.append(res)
#     pre=i
# print(re)

#
# l.sort()
# print(l)
# print(l[1])

# min=l[0]
# for i in l:
#     if i<min:
#         min=i
#     else:
#         pass
# print('minimum value in a list ',min)

#
# l = [10, 20, 4, 45, 99]
#
# for i in l:
#     if i %2==0:
#         print(i,end=' ')

# n=11
# m=20
# if n%2 != 0:
#     n=n+1
# for i in range(n,m,2):
#     print(i)


# li = [10, -21, 4, -45, 66, -93, 1]
# pos=0
# ne=0
# for i in li:
#     if i >0:
#         pos=pos+1
#     else:
#         ne+=1
# print("positive count is {} and negative count {}".format(pos,ne))

# li = [11, 5, 17, 18, 23, 50]
# ele=[5,18,50]
# for i in ele:
#     li.remove(i)
# print(li)

# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
#           ('krishna', 'akbar', '45'), ('',''),()]
# ls=[i for i in tuples if i]
# print(ls)
# l = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# dup={}
# for i in l:
#     if i in dup:
#         dup[i]+=1
#     else:
#         dup[i]=1
# print(dup)
#
# for key,values in dup.items():
#     if values >1:
#         print(key,end=' ')
#
# t= [5, 6, [], 3, [], [], 9]
# ls=[i for i in t if i ]
# print(ls)
# test_list= ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]
# key_list=["name","id"]
# n=len(test_list)
# res = []
# for idx in range(0, n, 2):
#     res.append({key_list[0]: test_list[idx], key_list[1] : test_list[idx + 1]})
# print(res)


# te = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
# di={}
# for i in te:
#     di[tuple(i[:2])] = tuple(i[2:])
# print(di)

        #
        # res = dict()
        # for sub in test_list:
        #     res[tuple(sub[:2])] = tuple(sub[2:])

# l=[[4, 1, 6], [7, 8], [4, 10, 8]]
# for i in l:
#     i.sort(reverse=True)
# print(l)

# test_list = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
# res = []
# for sub in test_list:
#     res.append([[ele, sub[-1]] for ele in sub[:-1]])
#
# print(res)
#
# input_list = [1, 2, 2, 5, 8, 4, 4, 8]
# lst=[]
# count=0
# for i in input_list:
#     if i not in  lst:
#         count+=1
#         lst.append(i)
#
# print(count)
# print('the unique values are :',lst)
#
# test_list = [1, 3, 5, 6, 3, 5, 6, 1]
# re=[]
# for i in test_list:
#     if i not in re:
#         re.append(i)
#
# print(re)
# pro=1
# for ele in re:
#     pro*=ele
#
# print(pro)
#
# import functools
# ls=functools.reduce(lambda x,y:x*y,set(test_list))
# print(ls)
#
# test_list = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]
# dup={}
# res=[]
# for i in test_list:
#     if i in dup:
#         dup[i]+=1
#     else:
#         dup[i]=1
# print(dup)
#
# for i,v in dup.items():
#     if v >=3:
#         res.append(i)
# print(res)
# arr = [4, 5, 5, 5, 3, 8]
#
# for i in range(len(arr)-2):
#     if arr[i]==arr[i+1] and arr[i+1]==arr[i+2]:
#         print(arr[i])
# arr1 = [1,2,2,3,4,5]
# arr2=[]
# for i in range(1,len(arr1)):
#     r=max(arr1[i],arr1[i-1])
#     arr2.append(r)
#
# print(arr2)
# l=[1,2,3]
# l1=[0,9,5]
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             if i != j and j != k and k != i:
#                 print(l1[i],l1[j],l1[k])

# test_list = ["geekforgeeks", [5, 4, 3, 4], "is",
#              ["best", "good", "better", "average"]]
# for i in test_list:
#     for j in range(4):
#         print(i,test_list[j])

# test_list = [(4, 5, 6, 3), (5, 6, 6, 9), (1, 3, 5, 6), (6, 6, 7, 8)]
# for i in test_list:
#     for j in range(len(i)-2):
#         if i[j] == i[j+1]:
#             test_list.remove(i)
#
# print(test_list)

# test_list1 = [[4, 3, 5, ], [1, 2, 3], [3, 7, 4]]
# test_list2 = [[1, 3], [9, 3, 5, 7], [8]]
# for i,j in zip(test_list1,test_list2):
#     print(i+j)

# su=[]
# for i in test_list:
#     su.append(sum(i))
# print(su)
# test_list = [[1, 4, 3, 1, 3], [3, 4, 5, 2, 4],
#              [23, 5, 5, 3], [2, 3, 5, 1, 6]]
#
# i,j=1,3
# res=sorted(test_list,key=lambda row: sum(row[i:j]))
# print('the sorted list ',res)

# test_list = ["geeks", "for", "geeks", "is", "best"]
#
# for i in test_list:
#     print(i[::-1],end=' ')
# k='g'
# test_list = ["Gfg is best", "Gfg is for geeks", "I love G4G"]
# res=[]
# for sub in test_list:
#     temp=sub.split()
#     for ele in temp:
#         if ele[0].lower() == k.lower():
#             res.append(ele)
#
# test_list = ['Gfg is best', 'for Geeks', 'Preparing']
# fi=[]
# for ele in test_list:
#     sub=ele.split()
#     fi.extend(sub)
# print(fi)
#
# l=[(1,2),(3,4),(5,6),(5,6),(8,9)]
# lst=[]
# for tpl in l:
#     for ele in tpl:
#         print(ele,end=" ")
#         lst.append(ele)
# print(lst)

# lst=['G', 'F', 'G', 'I', 'S', 'B', 'E', 'S', 'T']
# rep='$'
# ret='G'
# l=[]
# for i in lst:
#     if i == 'G':
#         l.append(i)
#     else:
#         l.append('$')
#
# print(l)
# test_list = ['gfg', '   ', ' ', 'is', '            ', 'best']
# res=[]
# for ele in test_list:
#     if ele.strip():
#         res.append(ele)
# print(res)
# test_list = [['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]
# ls=[]
# for sub in test_list:
#     for ele in sub:
#         print(ele)
#         ls.append(ele)
# print(ls)
# output=''.join(ls)
# print(output)

# test_list = ['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms']
# sub='Geek'
# res=len([i for i in test_list if sub in i])
# print(res)
# n=int(input('enter a number'))
# for i in range(2,n):
#     if(n%i==0):
#       print('it is not a prime number')
#       break
# else:
#   print('its a prime number')
#
# def isprime(n):
#     if (n == 1 or n == 0):
#         return False
#     # Run a loop from 2 to n-1
#     for i in range(2, n):
#         # if the number is divisible by i, then n is not a prime number.
#         if (n % i == 0):
#             return False
#         # otherwise, n is prime number.
#     return True
#
# N=100
# m=50
# for i in range(m,N+1):
#   #check if current number is prime
#   if(isprime(i)):
#     print(i,end=" ")
#
# def fab(x):
#     n = 20
#     l = [0, 1]
#     for i in range(n - 2):
#         next = l[i] + l[i + 1]
#         l.append(next)
#     if x in l:
#         return True
#     else:
#         return False
#
# a=fab(20)
# print(a)

# sum=0
# for i in range(5):
#     sum=sum+i**2
#     print(i)
#
# print(sum)
# n=123456
# res=0
# while n !=0:
#     res=res*10+n%10
#     n=n//10
#
# print(res)

# str='geeks quiz practice code'
# ls=str.split()
# print(' '.join(ls[-1::-1]))

# s = "This is a python language"
# ls=s.split(' ')
# lst=[]
# for i in ls:
#     if len(i)%2==0:
#         lst.append(i)
# print(' '.join(lst))

# str='geeksforgeek'
# n=int(len(str)/2)
# print(n)
# res=str[:n]
# res1=str[n:].upper()
# output=res+res1
# print(output)

# s='hello world'
# r=s[0].upper()+s[1:-1]+s[-1].upper()
# print(r)
import re

# str1 = 'abcdef'
# str2 = 'defghia'
# r=[]
# for i in str1:
#     for j in str2:
#         if i == j:
#             r.append(j)
# print(r)
#
# s='GeeksforGeeks'
# count=0
# for i in s:
#     if i in ('a','i','o','u','e'):
#         count=count+1
#
# print(count)
#
# s='geeksforgeeks'
# dup=[]
# un=[]
# for i in s:
#     if i not in dup:
#         dup.append(i)
#     else:
#         un.append(i)
# print(''.join(dup))
# print(''.join(un))
#
# test_str = "GeeksforGeeks"
# dic={}
# for i in  test_str:
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i]=1
#
# print(dic)
# res=max(dic,key=dic.get)
# print(res)

# string = "14, 625, 498.002"
# s=string.replace(',','comma')
# print(s)
# m=s.replace('.',',')
# res=m.replace('comma','.')
# print(res)
#
# str = 'ABC'
# for i in str:
#     for j in str:
#         for k in str:
#             if i !=k and j != i and j !=k:
#                 print(i,j,k,)

# test_list = [4, 7, 8, 3, 2, 1, 9]
# res='$'.join(map(str,test_list))
# print(res)

# test_str = "gfggfggfggfggfggfggfggfg"
# k='gfg'
# temp=len(test_str)//len(str(k))
# res=[k] * temp
# print(res)

# test_string = "GeeksforGeeks is best for geeks"
# word='best'
# l=test_string.split()
#
# for i in l:
#     if i == word:
#         break
#     else:
#         print(i,end =' ')
# import re
# str='man sun mop run'
# res=re.findall(r'm\w\w',str)
# print(res)
# str = 'anil akhil anant arun arati arundhati abhijit ankur'
# res=re.findall(r'a[nk][\w]*',str)
# print(res)
# s = 'Vijay 20 1-5-2001, Rohit 21 22-10-1990, Sita 22 15-09-2000'
# res=re.findall(r'\d{1,2}-\d{1,2}-\d{1,4}',s)
# print(res)
#
# test_str='<b>Gfg</b> is <b>Best</b>. I love <b>Reading CS</b> from it'
# tag='ba'
# reg_str = "<" + tag + ">(.*?)</" + tag + ">"
# res = re.findall(reg_str, test_str)
#
# print(res)
# importing re module
import re
# # initializing string
# test_str = '<b>Gfg</b> is <b>Best</b>. I love <b>Reading CS</b> from it.'
#
# # printing original string
# print("The original string is : " + str(test_str))
#
# # initializing tag
# tag = "b"
#
# # regex to extract required strings
# reg_str = "<" + "b"+ ">(.*?)</" + "b" + ">"
# res = re.findall("<" + "b"+ ">(.*?)</" + "b" + ">", test_str)
# # printing result
# print("The Strings extracted : " + str(res))
# str='AAAABBBBCCC'
# res=re.findall(r'(.)\1\1\1',str)
# print(res)

# email=input('enter :')
# reg=r'[a-zA-Z0-9.%_+]+@[a-zA-Z.-]+[.][a-zA-z]+'
# if (re.fullmatch(reg,email)):
#     print('valid')
# else:
#     print('invalid')
#
# res=re.sub(r'e{2,}','e','geeksforgeeks')
# print(res)
# x={'Alice' : 18}
# y={'Bob' : 27, 'Ann' : 22}
# z = {**x,**y}
# print(z)
#
# a,*b = [1, 2, 3, 4, 5]
# print(a)
# print(b)
#
# l=list(zip(*[('Alice', 'Bob'),
# ('Anna', 'Jon')]))
# print(l)
#
# l=[8,32,42,5,1]
# lst=sorted(l,key=lambda x: 0 if x==42 else x)
# print(lst)

# n=5
# p=1
# for i in range(n):
#     for j in range(i+1):
#         print(p,end=' ')
#     p+=1
#     print()
# n=5
#
# for i in range(0,n):
#     p = 0
#     for j in range(0,i+1):
#         print(p,end=' ')
#         p+=1
#     print()


# n=int(input('enter a number'))
# n=int(input('enter a number'))
# temp=n
# sum=0
#
# while n > 0:
#     digit=temp%10
#     sum+=digit**3
#     temp=temp//10
#
# if sum == n:
#     print('true')
# else:
#     print('false')
#
# n=int(input('enter a number'))
# sum=0
# temp=n
# while n >0:
#     digit=n%10
#     sum+=digit**3
#     n=n//10
# print(sum)
# n=int(input('enter a number'))
# rev=0
# while n !=0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
#
# print(rev)
# n=int(input('enter a number'))
#
# for i in range(2,n):
#     if n%i==0:
#         print('not a prime number')
#         break
# else:
#      print('prime numner')
# break stmt is used to break the loop execuation based on some condition
# we can use continue stmt to skip the current iteration
# and continue next iteration
#continue stmt is usedto skip the current
# iteration and continue the next iteration

#
# s=input('enter a string:')
# sub=input('enter a charector:')
# pos=-1
# n=len(s)
# while True:
#     pos=s.find(sub,pos+1,n)
#     if pos==-1:
#         break
#     print('found at position ',pos)
# n=int(input('enter a number'))
# for i in range(2,n+1):
#     if n%i ==0:
#         print('not prime')
#         break
# else:
#     print('prime')

# to check the number is prime or NOT
# n=int(input('enter a number'))
# for i in range(2,n):
#     if(n%i==0):
#       print('it is not a prime number')
#       break
# else:
#   print('its a prime number')

# start = 10
# end = 20
#
# print("Prime numbers between", start, "and", end, "are:")
#
# for num in range(start, end + 1):
#    # all prime numbers are greater than 1
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)
# l=[1,2,3,4,[1,2]]
# ls=[]





