#class and objects
#two type of instance methods
#accessor method /getter method--is a method that reads instance vars
#getXXXX() == getid(),getname(),getsalary()

#mutator method/setter method: is a method that not only reads the instance vars but also modify them
#setXXX(0 -- setid(0,setAddress,setdeptname()
class student:
    #properties or var
    def __init__(self,rno, name, marks):
        self.rno = rno   #instance variables:these are the vars whose separate copy is available to every object
        self.name = name  #instance variables
        self.marks = marks  #instance variables

    #methods
    def display(self):   #instance method:a method that acts on instance vars is known as instance method
        print('Roll no =', self.rno)
        print('Name = ', self.name)
        total=sum(self.marks)
        print('Total marks =', total)
        percentage=total/len(self.marks)
        print('percentage marks=%.2f%%' % percentage)

'''id = int(input('enter id:'))
name = input('enter name: ')
lst = [int(i) for i in input('enter marks with comm: ').split(',')]
s = student(id,name,lst)
s.display()'''

s1 = student(33,'mahesh',[70, 20, 95])
s1.display()
#accessor and muttor method

class Emp:
    def __int__(self):
        self.id=1001
        self.name ='MALLI'

    #ACCESSOR METHOD
    def getId(self):
        return self.id
    def getName(self):
        return self.name

e = Emp()
print('id =',e.getId())
print('ename =',e.getName())