#BIGGEST IN THREE NUMBER

a=int(input('Enter first number: '))
b=int(input('Enter Second number: '))
c=int(input('Enter third number: '))

if a>b:
    if a>c: max = a
    else: max = c
else:
    if b>c: max = b
    else:  max = c
    
print('bigger=',max) 
