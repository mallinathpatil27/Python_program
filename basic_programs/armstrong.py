n=int(input('enter a number'))

temp=n
rev=0

while temp != 0:
    digit=n%10
    rev=rev*10+digit
    temp=temp//10

print(rev)    
