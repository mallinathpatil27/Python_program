'''j=lambda inp: False if (inp=='sum' or inp == 'q' or inp == 'x') else  lst
    print(obj(inp))'''

ops=['sum','+','diff','-','mul','*','div','/']
lst=[]
a=True

while a == True:
    inp=input('Enter any string or number:')
    if inp in ('exit','q','x'):
        a = False
    elif inp in ops:
        print(lst)
        if inp in ('sum','+'):
            print('Total sum is: ',sum(lst))
            lst.clear()
        elif inp in ('diff','-'):
            d = max(lst)-min(lst)
            print("diff in max & min values is",d)
            lst.clear()
        elif inp in ('mul','*'):
            n = 1
            for e1 in lst:
                n = n* e1
            print('product of elements :',n)
            lst.clear()
        elif inp in ('div','/'):
            di=max(lst)/min(lst)
            print('division',di)
            lst.clear()
        else:
            print('wrong')
    elif int(inp) <=10000000:
        lst.append(float(inp))


