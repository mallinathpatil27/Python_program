#to check whether the element exits or not in the list
lst=[1,2,3,4,5,6,7,8,9,0,10]
s=int(input('enter the number:'))

for i in lst:
    if s==i:
        print('the number is exits')
        break
else:
    print('the no is not exits')