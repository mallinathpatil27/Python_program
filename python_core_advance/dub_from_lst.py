#removing the duplicate elements  from the list
lst=[]
lst1=[]
n=int(input('how many elements?:'))
#taking input elemnets from user appending it into list
for i in range(n):
    s =input('enter the elemnents:')
    lst.append(s)
print('your entered elements are:',lst)

#removing the dublicate from list
for x in lst:
    if x not in lst1:
        lst1.append(x)
#printing the final list after remving dublicate from the list
print('The elements after removing dublicate is :',lst1)