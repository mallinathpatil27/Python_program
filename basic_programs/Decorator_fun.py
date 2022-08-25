#Decorator
#is a fun that Modifies the result of another func.
#it takes a fun as its parameter and return another fun
#decorator that increment the value of anothe func by 10

def decore(fun):
    def inner():
        res =fun()
        res =res+10
        return res
    return inner
@decore
def fun():
    return 100


n = fun()
print(n)


'''
name =decore(fun)
n = name()
print(n)
'''
