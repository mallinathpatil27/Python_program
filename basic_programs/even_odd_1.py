#even odd for floting values  inanother way
n=input('enter a number:')
s1=n.split('.')
s2=s1[1]

if s2[-1] == '0':
    if int(s2[-2]) % 2 == 0:
        print('even')
    else:
        print('odd')
    
elif int(s2) % 2 == 0:
    print('even')
else:
    print('odd')
    
