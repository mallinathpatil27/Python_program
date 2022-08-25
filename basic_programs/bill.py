#CALCULATING THE ELECTRICITY BILLS

previous=int(input('Enter the previos bill reading : '))
present=int(input('Enter the present reading: '))

units=present-previous
print('no of units : ',units)

if units <=100: bill=0
elif units <=300: bill = units*5
elif units <=500: bill = units*10
else:bill =units *12.50

print('Total bill =Rs.',bill)
