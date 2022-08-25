#we can assign  func to a var
#we can pass a fun to another func
#we can write a func inside another func
#we can return a func from another func

'''a function written inside another fun is called
inner fun or 'inside fun'''

def display():
    def inner():
        return 'malli'
    return 'hello'+inner()

str =display()
print(str)

