#we can assign  func to a variable
#we can pass a fun to another function
#we can write a func inside another func
def display(a):
    res = a()
    return 'hello'+res

def b():
    return 'naagu'

str = display(b)
print(str)
