#printing the even nos  between m and n numbers
m,n=[int(i) for i in input('enter start,stop:').split()]
x=m
if x%2 !=0:x=m+1 # start from min
while x<=n:
    print(x)
    x=x+2
