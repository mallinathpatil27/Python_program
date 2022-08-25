#to find addition and substrcation
def add_sum(a,b):
     res1=a+b
     res2=a-b
     return res1,res2

a= int(input('enter a numbe:'))
b=int(input('enter a number:'))

r1,r2 = add_sum(a,b)
print('result of addition =',r1)
print("result of substraction =",r2)


#list
ls=['sdf',23,'safs',8,5,'sdfsd',8,'sdfs',56,21,'sfs',20,5]

number=sorted([int(x) for  x in ls if x.isdigit()])
print(ls)
print(number)

