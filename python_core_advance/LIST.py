#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
def last(n):return n[-1]

def sort_lst(tupl):
    return sorted (tupl,key=last)

print(sort_lst([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

#Write a Python function that takes two lists and returns True if they have at least one common member.

array = [[ ['*' for col in range(6)] for col in range(4)] for row in range(3)]
print(array)

#Write a Python program to generate all permutations of a list in Python.

import itertools
print(list(itertools.permutations([1,2,3,5])))

#Write a Python program access the index of a list.
nums = [5, 15, 35, 8, 98]
max = nums[0]
for num_index, num_val in enumerate(nums):
    if num_val > max:
        max =num_val

print(max,nums.index(max))

#Write a Python program to flatten a shallow list.
import itertools
original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
new_merged_list = list(itertools.chain(*original_list))
print(new_merged_list)

#Write a Python program to get the frequency of the elements in a list.

import collections
my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
print("Original List : ",my_list)
ctr = collections.Counter(my_list)
print("Frequency of the elements in the List : ",ctr)
#output :{10: 4, 20: 4, 40: 2, 50: 2, 30: 1}

#Write a Python program to find the second largest number in a list.
lst=[1, 1, 1, 0, 0, 0, 2, -2, -2]

lst.sort()
print(lst[-2])

#find the subset prsent in it or not
a = [2,4,3,5,7]
b = [4,3]
c = [3,7]
if set(a) >= set(c):
    print('True')
else:
    print('False')

#Write a Python program to create a list by concatenating a given list which range goes from 1 to n.

my_list = ['p', 'q']
n = 4
new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in my_list]
print(new_list)

#Write a Python program to convert a list of multiple integers into a single integer.
L = [11, 33, 50]
print("Original List: ",L)
x = int("".join(map(str, L)))
print("Single Integer: ",x)
#output: 113350

#Write a Python program to generate groups of five consecutive numbers in a list.

l = [[5*i + j for j in range(1,6)] for i in range(5)]
print(l)
#output:[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

#Write a Python program to split a list every Nth element.

C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
def lst(S, step):
    return [S[i::step] for i in range(step)]
print(lst(C,4))

#zip objects

for i,j in zip(range(5),range(5,1,-1)):
    print(i,j)

#Write a Python program to find the list in a list of lists whose sum of elements is the highest.

my_list = [{},{},{}]
my_list1 = [{1,2},{},{}]
print(all(not d for d in my_list))
print(all(not d for d in my_list1))

#Write a Python program to remove consecutive (following each other continuously) duplicates (elements) of a given list.

from itertools import *
def compress(nums):
    return [x for x,group in groupby(nums)]
n_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ]
print(n_list)

#Write a Python program to pack consecutive duplicates of a given list elements into sublists.
from itertools import groupby
def pack_consecutive_duplicates(l_nums):
    return [list(group) for key, group in groupby(l_nums)]
n_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ]
print("Original list:")
print(n_list)
print("\nAfter packing consecutive duplicates of the said list elements into sublists:")
print(pack_consecutive_duplicates(n_list))

#Write a Python program to create a 3X3 grid with numbers.

nums = []
for i in range(3):
    nums.append([])
    for j in range(1, 4):
        nums[i].append(j)
print("3X3 grid with numbers:")
print(nums)



