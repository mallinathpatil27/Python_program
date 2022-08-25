#accept a group of number find there sum and average

lst = [int(i) for i in input('enter nos:').split()]

print(lst)
s = sum(lst)
print('sum:',s)

AVG=s/len(lst)

print('avg=%.2f' %AVG)
