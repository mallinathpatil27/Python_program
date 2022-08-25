# TO FIND THE BIGGEST NUMBER IN 3 NUMBERS
a=int(input('a= '))
b=int(input('b= '))
c=int(input('c= '))

if a>=b and a>=c : max =a
elif b>=c and b>=a: max = b
elif c>=b and c>=a: max = c

print('Bigger=',max)
