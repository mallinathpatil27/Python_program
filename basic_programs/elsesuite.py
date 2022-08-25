#to given number is there in lst r not
lst=[10,20,30,40,50]

n=int(input('enter a nos:'))

for i in lst:
    if n==i:
        print('found')
        break
else:
    print('Not found')

    
