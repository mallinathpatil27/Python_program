# Derive rectangle class from square class from rectangle
class area:
    def __init__(self,x):
        self.x=x

    def area(self):
        area=self.x*self.x
        print("the area of square is :",area)

a=area(10)
a.area()
class rectangular(area):
    def __init__(self,x,y):
        super().__init__(x)
        self.y=y

    def area1(self):
        super().area()
        area=self.x * self.y
        print("area of the rectangle is ",area)
s=rectangular(10,8)
s.area1()
class area:
    def __init__(self,x):
        self.x=x

    def area(self):
        area=self.x*self.x
        print("the area of squre is ",area)

s=area(20)
s.area()
class recta(area):
    def __init__(self,x,y):
        super().__init__(x)
        self.y=y

    def area(self):
        super().area()
        area=self.x* self.y
        print("the are of rectangl is ",area)
x=recta(30,40)
x.area()

# #Area
# class Area:
#     def __init__(self,x):
#         self.x = x
#
#     def area(self):
#         A=self.x * self.x
#         print('area of square : ',A)
#
# s=Area(1)
# s.area()
#
# class Rectangl(Area):
#     def __init__(self,x,y):
#         super().__init__(x)
#         self.y=y
#
#     def area(self):
#         super().area()
#         area=self.x * self.y
#         print('area is =',area)
#
# s=Rectangl(23 ,4)
# s.area()


# class Add:
#     def __init__(self):
#         self.a=10
#         self.b=20
#
#     def sum(self):
#         sum= self.a +self.b
#         print(sum)
#
#     def call_talk(obj):
#         obj.talk()
#
# s=Add()
# call_talk(s)
