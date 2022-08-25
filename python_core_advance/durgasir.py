import re
# f1=open("D:/pandas/emp.txt","r")
# f2=open("D:/pandas/outpu.txt","w")
# # f2.write("this s bull shit \n ")
# for line in f1:
#     list=re.findall("[7-9]\d{9}",line)
#     for n in list:
#         f2.write(n+"\n")
# print("extracted all mobile number successfully you can go and see")
# f1.close()
# f2.close()

'''
str='azbc bcd bacd azcbd abzcdm abzdbh zjd absbj'
result=re.findall(r'\w*z.\w*',str) # to find the  a word conatining z.
print(result)


#the letter z not containing at the bigining or ending of the word
str='mallila'
res=re.search(r'\Bz\B',str)  #\B  signifies no blank space at begining and end of the line
if res:
    print('True')
else:
    print('False')

ip = "0216.08.094.1960"
str=re.sub('\.[0]*','.',ip)   # it will remove the leading  zeros
print(str)

#find the word occurance and its positions
text='Python exercises, PHP exercises, C# exercises'

pattern='exercises'
matcher=re.finditer("exercises",text)
for match in matcher:
    print(match.start(),':',match.end())

#to change the date formate one formate to another formate
date="2026-01-02"
date1=re.sub(r'(\d{4})-(\d{2})-(\d{2})','\\3-\\2-\\1',date)
print(date1)

# output: 02-01-2026

text = "Ten 10, Twenty 20, Thirty 30"
result = re.split("\D+", text)
print(result)
# Print results.
for element in result:
    print(element)

#Write a Python program to split a string at uppercase letters.

text = "PythonTutorialAndExercises"
print(re.findall('[A-Z][^A-Z]*', text))

#String concepts
s="Learning Python is very very easy!!!"
lst=s.split(' ')
lst1=[]
for i in lst:
    lst1.append(i[::-1])
print(lst1)
output=' '.join(lst1)
print(output)


s = "abcabcabcabcadda"
print(s.count('a'))

s="durga huli"
o=''.join(reversed(s))
print(o)

m='Learning Python is very Easy'
l=m.split(' ')
l1=[]
for i in l[::-1]:
    l1.append(i)
out=' '.join(l1)
print(out)

s=input("enter the string:")
s1=s2=output=''
for x in s:
    if x.isalpha():
        s1=s1+x
    else:
        s2=s2+x

for x in sorted(s1):
    output=output+x
for m in sorted(s2):
    output=output+m
print(output)


s=input("enter the string:")
output=''
for x in s:
    if x.isalpha():
        output=output+x
        previous=x
    else:
        output=output+ previous *(int(x)-1)
print(output)

n=[1,2,3,4,5,6]
n.insert(2,123)
print(n)


n=[1,2,3,4,5,6,2,2,2,2]
# lst=n.remove(2)
while 2 in n:
    n.remove(2)
print(n)

list=[[10,20,30],[40,50,60],[70,80,90]]

fla=[i for i in list for i in i ]
print(fla)

words="the quick brown fox jumps over the lazy dog".split()
print(words)
l=[[w.title(),len(w)] for w in words]
print(l)
m=[[w.title(),w[0].upper()] for w in words]
print(m)

str="mallinath"
s=[[x.upper()] for x in str]
print(s)


# to check the valid mobile number or not
n=input("enter the mobile number to check :")
m=re.fullmatch("[7-9]\d{9}",n)
if m!=None:
    print("found")
else:
    print("not found")


f1=open("d:/pandas/malli.txt","r")
f2=open("d:/pandas/phone.txt","w")
for line in f1:
    list=re.findall("[7-9]\d{9}",line)
    for n in list:
        f2.write(n+"\n")

print("succefully extracted all the phone number")
f1.close()
f2.close()
s= input("enter the mail id:")
m=re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",s)

if m!=None:
    print("found")
else:
    print("not found")
def text_match(text):
    pattern='^a(b*)$'
    if re.search(pattern,text):
        return "found"
    else:
        return('not found')

print(text_match("abc"))

#Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re
s=input('enter a pattern to check:')
m=re.search(r"[A-Z]+[a-z]+$",s)
if m!= None:
    print("found")
else:
    print('not found')

#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
s=input('enter a pattern to check:')
m=re.search(r"a*b$",s)
if m!= None:
    print("found")
else:
    print('not found')

lst=[1,2,3,4,5,6,7,8,9,10,11,12,13]
print(len(lst))
for i in range(0,10,2):
    lst.pop(i)
    print(lst[i])
    lst.pop(i)
print(lst)
'''

ip = "0216.08.094.1960"
str=re.sub('\.[0]*','.',ip)   # it will remove the leading  zeros
print(str)
str1=re.sub('.','',ip)

print(str1)
str="geeksforgeeks"
dict={}
for i in str:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
s="mallinath"
l1=l2=[]
for i in range(0,len(s)):
    if i % 2 ==0:
        l1.append(s[i].upper())
    else:
        l1.append(s[i])
output=''.join(l1)
print(output)
print(l1)

x=3
print("formatted :{:*<4d}".format(x))
y=1234567
print("formatted :{:,}".format(y))

str1="geeksforgeek"
vowels="aeiouAEIOU"
l=[w for w in str1 if w in vowels]
print(l)

#finding the largest length of element and its length
str2="Write a Java program to sort an array of given integers using Quick sort Algorithm"
lst=str2.split()
max=len(lst[0])
l1=[]
print(max)
for i in lst:
    if len(i) > max:
        max=len(i)
        l1.append(i)
    else:
        pass
print(l1[-1],max)
print(max)

# deleting all occurancw of a string
# def delete_all_occurrences(str1, ch):
#     result = str1.replace(ch, "")
#     return (result)


