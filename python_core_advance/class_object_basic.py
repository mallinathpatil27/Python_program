
#class and objects
#what happened when object is created.
#PVM allocates memory.
#PVM store object mem address into self.
#pvm executes the constructor.
#PVM return the memory address of the objects.
#self is a variable that is created by pvm to store the current object location or memory address
#constructor is a special  method to create a instance vars.it will executes during the process of creating the objects

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
print(person.__doc__)
print(s)
'''
#two types of constructor
#default parameters or zero parameterized : it is use to intialize all the objects with same data
#parameterized constructor : is a constructor with one or more parameters .it is useful to intialize the every
#objects with differnt data.

#create  a student class with rno,nam,address and marks in 5 subjects

class Student:
    def __init__(self):
        self.rno=100
        self.name='sathis'
        self.marks=[98,98,78]

    def display(self):
        print('The student roll no',self.rno)
        print('The student name ',self.name)
        tot = sum(self.marks)
        print('total marks  of all subjects',tot)
        perc = tot/len(self.marks)
        print('percentage marks = %.2f ' %perc)
        print('The student marks  ',self.marks)

s=Student()
print(s.display())

class Student:
    def __init__(self, rno, name, marks):
        self.rno = rno
        self.name = name
        self.marks = marks

    def display(self):
        print('The Student Roll no', self.rno)
        print('The Student name', self.name)
        print('The Student marks', self.marks)


m = Student(100, 'amar', [90, 89, 70])
m.display()

n = Student(100, 'chaitanya', [90, 89, 70])
n.display()
'

print('---------------------------------------------')

def display(rlno,name,marks):
    print('his name =',name)
    print('his ro roll no',rlno)
    print('his marks',marks)

s=display(100,'mahesh',[19,90,90])
print(s)

#if annaul salary is <= 250000 then income tax =0
#if anual sal > 250000 then income tax =10%
#HRA=15.5% of annaul salary'''