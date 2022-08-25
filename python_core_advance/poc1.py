# reversing the intiger values
n = 12345
print("before reverse your numeber is : %d " %n)
reverse = 0
while n!=0:
    reverse = reverse*10 + n%10
    n = (n//10)
print("After reverse : %d" %reverse)


# reading the docs in  function
class student:
    '''this is student class'''

print(student.__doc__)
help(student)