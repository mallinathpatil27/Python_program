# to find the sum and average of three numbers

a,b,c=[float(x) for x in input('enter the three numbers:').split()]

d,e,f=[int(i) for i in input("enter another three numbers with comma :").split(',')]

sum1=a+b+c
avg1=(a+b+c)/3
sum2=d+e+f
avg2=sum2/3
print('the sum of three no is',sum1)
print('the avg of three nos is=%.2f' %avg1)
print('the sum of the nos ',sum1)
print('the avg of the nos=%.2f'% avg2)
