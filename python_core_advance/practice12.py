# Write a Python program to find the set of distinct characters in a given string, ignoring case

def test(str):
    return [*set(str.lower())]

t=test("HELLO")
print(t)

#Write a Python program to find all words in a given string with n consonants.

def test(str,n):
    return [i for i in str.split() if sum ([c not in 'aeiou' for c in i.lower()]) == n]

t1=test("this is our time",3)
print(t1)

#Write a Python program to find all even palindromes up to n.
def pali_even(n):
    return[i for i in range(0,n) if str(i) == str(i)[::-1]] # if we write str(i[::-1]) it will not work

m=pali_even(100)
print(m)

# Given an array of numbers representing a branch on a binary tree, write a Python program to find the minimum even value and its index. In the case of a tie, return the smallest index. If there are no even numbers, the answer is [].

def array(nums):
    even=[]
    odd=[]
    for i in range(len(nums)):
        if (nums[i] % 2 == 0):
            even.append(nums[i])
        else:
            odd.append(nums[i])
    print(min(even))

s=array([1, 9, 4, 6, 10, 11, 14, 8])
print(s)

#another way to find the min values

def array_min(nums):
    if any(n%2 == 0 for n in nums):
        return min([v,i] for i,v in enumerate(nums) if v%2 == 0 )
    else:
        return []
s=array_min([1, 9, 4, 6, 10, 11, 14, 8])
print(s)

# Write a Python program to find the even-length words from a given list of words and sort them by length.
def test(words):
    for w in words:
        if len(w) % 2 ==0:
            print(w,end=" ")
t1=test(["Red", "Black", "White", "Green", "Pink", "Orange"])
print(t1)

#another easy way
def test(words):
    return sorted([w for w in words if len(w) % 2 == 0],key=lambda w:(len(w),w))

t1=test(["Red", "Black", "White", "Green", "Pink", "Orange"])
print(t1)

# Write a Python program to find the first n Fibonacci numbers.
def test(n):
    a = [1, 1]
    while len(a) < n:
        a += [sum(a[-2:])]
    return a[:n]
t1=test(15)
print(t1)