#Arrays topics: collection of homegeneios objects
#types
#1D Arrays
#multi D arrays
#=------
#single dimensions :only 1 row or 1 col of elements
'''  all array should have the uniform datatype
to create array we use
1.array() functiom:
import numpay as np
arr=np.array([10,20,30])
for i in arr:print(i)

2.linspace():we can create array
x=np.linspace(0,10,5 )

3.logspace()
x=np.logspace(1,4,5)#here 1 means 10 power 1
datascince used this type if linespace

4.arange()
x=np.arrange(10)
same as range functions
y=np.arrange(10,20,2)

5.zeros() : all zero as element
x=np.zeros(6,int)
o/p=array([0,0,0,0,0,0])  (here float is default datatype )
 and ones()

 arr+5= it will add 5 to the all elements
 arr*2=it will multiply the all elements with 2
 np.power(arr,3)= to find the pwoer of 3
 sum(arr)
 max(arr)
 min(arr)
 np.argmin(arr)=positioon of min elements
 np.argmax(arr)= position of max elements
 np.sort(arr)=in ascending order
 np.sort(arr)[::-1] it will sort into descending order
 OPERATIONS ON 1D
 arr[0],arr[1]---indexing is possible
 arr[0:3]---slicing also possible
 but repetation is not possible
--
arr=array([20,10,35,40])
print(arr)
x=arr.view()=to copy the all elemnts of array.it is called shallow copy
shallow coping is nothing but coping the elements of one array to the other
array both the array work like same array if any modification to one array
it will effects another array also in this we use view method

copy method or deep coping
in this any modification to one array other array will not effect
x=arr.copy()= in this there is no connection between to the two arrays

ATTRIBUTES OF AN ARRAY:(properties)
1.ndim:it will give you dimensionality of array
arr.ndim=it will show the type of array

2.shape =no of elements in 1d,and no of rows ,columns in 2d
arr.shape

3.size =no of elements in array:

4.item size :size of one elements it will give u size in bytes
5.nbytes: total size of array one bytes X total number of elemnets

6.dtype=gives the datatype of array
  arr.dtype

7.reshape:it converts 1D to 2D
   arr.reshape(1,3) or (3,1)
8.flatten : 2D to 1D array

2D ARRAYS: MORE THAN 1 ROW AND MORE THAT 1 COLUMNS
  arr=array([[1,2,3],[1,3,4],[4,6,7]])
  type(arr)=it will give numpay.ndarray(n dimensional array)

  using ones() and zeros() we create 2d array
  ones((3,4),float): its ALL elements are 1
  zeros((3,3),int)
  anothe one is EYE
  eye(4,dtype=int) in this all daigonal elements are 1

  OPERATIONS :
  indexing and slicing we can do here not repitations
  [1,2,3]==oth row  arr[0] it will give zeroth row all elements
  [1,2,3]-- 1st row  arr[1]
  [1,2,3] -- 2nd row  arr[2]
  arr[0,1] zeroth row 1st column elements it will retrive
   slicing = arr[r1:r2,c1:c2]
             arr[0:2,0:2]

  MATRICS:is collection of elemnts arranged in rows and columns
  row matrics
  columns matrics
  mxn matrics
  creating a matrix
  str ="10 20 30  40 50 60; 40 50 60"
  m1=matrics(str)
 m2=matrixs(arr)
 m1*m2 and m1+m2 we can do
 3 methods to find transpose
 m1.transpose
 m1.T =TO FIND TRANSPOSE
 m1.getT()
 d=diagonal(m1) to get diagonal elements
m1.max()
m1,min(0
m1.mean()
m1.sum()
sort(m2)=it will sort the row wise ie horizontally
sort(m2,axis=0) it will sort the column wise ie vertically
how to accept the elements from key board
r,c=[int(i) for i in input ('how many row,cols').split(',')]

#create a 2d array with r row and c cols with zeros
arr=zeros((r,c),int)
print('enter elements in matrixs:')
 for i in range(r):
     arr[i] =[int(x) for x in input.split() ]
  #converts 2d into matricx

  m=matrix(arr)
  m1=m.transpose
  '''
