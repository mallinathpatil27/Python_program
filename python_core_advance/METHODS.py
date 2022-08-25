#METHODS
class Emp:
    '''THIS IS BASIC CLASS EXAMPLE'''
    def __int__(self):
        self.id = 1001
        self.name ="malli"

    def getId(self):
        return self.id
    def getName(self):
        return self.name
    #ACCESSOR METHOD
    #mutator method

    def setId(self,id):
        self.id =id
    def setName(self,name):
        self.name =name

e=Emp()

'''id=e.getId()
print(id)
print("id=", e.getId())
'''

e.setId(1000)
e.setName('mahesh')
print("id",e.getId())
print('name=',e.getName())

#class method
class Myclass:
    x =10 #this is class variable or static vars

    @classmethod
    def modify(cls):
        cls.x+=1

m1=Myclass()
m2=Myclass()

print(m1.x,m2.x)

m1.modify()  #Myclass.modify()
print(m1.x,m2.x)

m1.x+=1
print(m1.x,m2.x)

#ro count the no of objects for a class
class myclass:
    x=0
    def __init__(self):
        myclass.x+=1
    @staticmethod
    def display():
        print('no of objects =',myclass.x)

n1=myclass()
n2=myclass()
n3=myclass()
n4=myclass()

myclass.display()


#to calculate squre root method
class myclass:
    @staticmethod
    def sroot(x):
        return x ** 0.5

res=myclass.sroot(16)
print(res)

#inner class demo
class Myclass:
    x = 0
    def __init__(self):
        Myclass.x+=1
    @staticmethod
    def display():
        print('no of objects ',Myclass.x)

m1=Myclass(__doc__)
print(m1)

m2=Myclass()
Myclass.display()






