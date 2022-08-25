'''to accept multiple values in single line
using lsit comprehension is createing new
list from an iterable object
'''

a,b,c = [int(i) for i in input('enter number:').split()]

tot=a+b+c

print(tot)
