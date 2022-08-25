# to reverse a number

num =int(input('Enter a number: '))
'''
while num != 0:
    digit = num %10   #removing the last number
    print(digit,end='')   # printing the last number only
    num =int(num/10)      # then deleting the last number and continuing the same

'''
st=str(num)
res=str[::-1]
print(res)
