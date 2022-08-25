#pallindrom or not
def palli(str):
    for x in str:
        if x== x[::-1]:
            print(True)
        else:
            print(False)

x=palli(['palindrome', 'madamimadam', '', 'foo', 'eyes'])
print(x)

#another easy way

def test(str):
    return [ s == s[::-1] for s in str]

t2=test(['palindrome', 'madamimadam', '', 'foo', 'eyes'])
print(t2)

#Write a Python program to find the strings in a given list, starting with a given prefix
def test(strs,prefix):
    return[s for s in strs  if s.startswith(prefix)]

strs=['cat', 'car', 'fear', 'center']
prefix="ca"
print(test(strs,prefix))

# Write a Python program to find the lengths of a given list of non-empty strings

def test(str):
    object=map(len,str)
    print(list(object))

test(['cat', 'car', 'fear', 'center'])

#another way
strs =  ['cat', 'car', 'fear', 'center']
result=map(lambda x : len(x),strs)
print(list(result))

# Write a Python program find the longest string of a given list of strings.

def test(str):
    return max(str,key=len)

t2=test(['cat', 'car', 'fear', 'center'])
print(t2)

#Write a Python program find the strings in a given list containing a given substring.
def sub(str,substr):
    return[s for s in str if substr in s]

t=sub(['cat', 'car', 'fear', 'center'],'ca')
print(t)

#separting with comma and space
def test(s):
    if " " in s:
        return s.split(" ")
    if "," in s:
        return s.split(",")
    return [c for c in s if c.islower() and ord(c) % 2 == 0]

t=test("abcd")
print(t)

#Write a Python program to determine the direction ('increasing' or 'decreasing') of monotonic sequence numbers

def seq(str):
    for i in range(len(str)):
        if str[i] < str[i+1]:
            return 'increasing'
        elif str[i] >  str[i+1]:
            return 'decreasing'
        else:
            return 'not monotonic'

t1=seq([19,19,5,5,5,5,5])
print(t1)
#another way

def test(nums):
    return "Increasing" if all(nums[i] <nums[i+1] for i in range(len(nums) - 1)) else \
        "Decreasing" if all(nums[i] >nums[i+1] for i in range(len(nums) -1 )) else \
        "Not a monotonic sequential !"
t1= test([6,5,4,3,2,1])
print(t1)

#Write a Python program to check, for each string in a given list, whether the last character is an isolated letter or not. Return True or False

def test(str):
    return [len(s.split(" ")[-1]) == 1 for s in str] #len(s.split(' ')[-1] it will split and give the last word
                                                     #if last word is equal to one then print true else false
t1=test(['ca t', 'car', 'fea r', 'cente r'])
print(t1)

# Write a Python program to compute the sum of the ASCII values of the upper-case characters in a given string
def test(strs):
    return sum(map(ord,filter(str.isupper,strs)))

t1=test("PytHon ExerciSEs")
print(t1)

#Write a Python program to create a list whose ith element is the maximum of the first i elements from a input lis

def test(nums):
    return [max(nums[:i]) for i in range(1,len(nums) + 1)]

t1=test([0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0])
print(t1)


# Write a Python program to find the largest number where commas or periods are decimal points

def test(nums):
    return max(float(s.replace(',','.')) for s in nums)

t1=test(['100', '102,1', '101.1'])
print(t1)

#Write a Python program to select a string from a given list of strings with the most unique characters.
def test(strs):
    return max(strs,key=lambda x:len(set(x)))
t1=test(['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique'])

print(t1)

#Write a Python program to find the list of strings that has fewer total characters (including repetitions)

def test(str):
    return min(str,key=lambda x: sum(len(i) for i in str)) # to find the min length string
    return max(str, key=lambda x: sum(len(i) for i in str))

t1=test([['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider']])
print(t1)


#Write a Python program to find the positions of all uppercase vowels (not counting Y) in even indices of a given string.

def test(str):
    return [i for i, c in enumerate(str) if i % 2 == 0 and c in 'AEIOU']
t1=test( "w3rEsOUrcE")
print(t1)

#Write a Python program to find the sum of the numbers of a given list among the first k with more than 2 digits.
i=4
def test(nums,k):
    s= 0
    for i in range(len(nums))[:k]:
        if len(str(abs(nums[i])))>2:
            s =s +nums[i]
    return s

t1=test([4, 5, 17, 9, 14, 108, -9, 12, 76],8)
print(t1)

#another easy way to find this
sum=0
def test(nums,k):
    sum=0
    for i in range(len(nums))[:k]:
        if nums[i] >=100:
            sum=sum+nums[i]
    return sum

t1=test([4, 5, 17, 9, 14, 108, -9, 12 ,76],10)
print(t1)

#another way to find this

def test(nums):
    sum=0
    for i in range(len(nums[:8])): #it will take length of nums i.e in range of 1 to 14
        sum = sum + nums[i]   #num[i] if i is o to 14 index it will retrive the o to len of number from the numns
        print(sum)
t1=test([4, 5, 17, 9, 14, 108, -9, 12 ,76])
print(t1)

# Write a Python program to compute the product of the odd digits in a given number, or 0 if there aren't any
def test(nums):
    if any(int(c) % 2 for c in str(nums)):
        prod=1
        for c in str(nums):
            if int(c) %2 ==1:
                prod=prod* int(c)
        return prod
    return 0
t1=test(123456789)

print(t1)

#Write a Python program to find the largest integer divisor of a number n that is less than n
def test(n):
    return next(c for c in range(n -1,0,-1) if n%c == 0 )

t1=test(18)
print(t1)

# Write a Python program to determine which triples sum to zero from a given list of lists

def test(nums):
    return [sum(t) == 0  for t in nums]

#t1=test([[1, 2, -3], [-4, 0, 4], [0, 1, -5], [1, 1, 1], [-2, 4, -1]])
#print(t1)

#41. Write a Python program to sort numbers based on strings.

def test(str):
    return ' '.join([x for x in 'one two three four five six seven eight nine'.split() if x in str])

t1=test("six one four one two three")
print(t1)



