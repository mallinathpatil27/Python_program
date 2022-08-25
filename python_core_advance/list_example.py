#Write a Python program to sum all the items in a list

def su(lst):
    sum=0
    for i in lst:
        sum=sum+i
    return sum

t=su([1,2,-8])
print(t)

#