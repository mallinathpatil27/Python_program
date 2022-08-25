#using the student class
from student import *
s=Student()
s.setId(100)
s.setName('malli')
s.setAddress('cidco n2')
s.setMarks(980)

print('id=', s.getId())
print('name', s.getName())
print('address', s.getAddress())
print('marks', s.getMarks())