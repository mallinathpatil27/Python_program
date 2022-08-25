
class Person:
    #properties = variable
    def __init__(self): # constructor is used to initialize the variables,and it is sp method to create instance vars
                        # self is default parameter,it stores the memory address of current objects.
        self.name = 'Srinu'
        self.age = 22

    #actions
    def talk(self):
        print('hello this is ',self.name)
        print('hello his age is',self.age)


s=Person()
print(s.talk())
print(s)
print(s.age)


def display(rlno,name,marks):
    print('his name =',name)
    print('his ro roll no',rlno)
    print('his marks',marks)

s=display(100,'mahesh',[19,90,90])
print(s)
