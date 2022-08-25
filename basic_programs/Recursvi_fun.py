#recursive function calling function itself

def fact(n):
    if n == 0:
        res = 1
    else:
        res = n*fact(n-1)
    return res

r= fact(4)
print('factorial :' ,r)
