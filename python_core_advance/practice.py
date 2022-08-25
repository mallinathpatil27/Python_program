def test(n):
    return [n + 2 * i for i in range(n)]

t=test(2)
print(t)

#Write a Python program to check the nth-1 string is a proper substring of nth string in a given list of strings.
def test1(str1):
    if str1[len(str1)-2] in str1[len(str1)-1] and str1[len(str1)-2] != str1[len(str1)-1]:
        return True
    else:
        return False
t1=test1(["a","abb","sfs", "oo", "de", "sfde"])
print(t1)

'''Write a Python program to test a list of one hundred 
integers between 0 and 999, which all differ by ten from one another. Return true or false.'''

def test(li):
    return all(i in range(1000) and abs(i - j) >= 10 for i in li for j in li if i != j) and len(set(li)) == 100

t=test([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990])

print(t)

#Write a Python program to check a given list of integers where the sum of the first i integers is i

def test(nums):
    return all([sum(nums[:i]) == i for i in range(len(nums))])

t=test([1,1,1,1,1,1])
print('result:',t)

#split function into words and separtot

def test(str):
    import re
    lst=re.split("([ ,]+)",str)
    word=lst[0::2]
    comma=lst[1::2]
    return comma,word

output = test("W3resource Python, Exercises.")
print(output)

output1 = test("The dance, held in the school gym, ended at midnight.")
print(output1)

#find list integers containing exactly four distinct values, such that no integer repeats twice consecutively among the first twenty entries

def test(nums):
    return all([nums[i] != nums[i+1]  for i in range(len(nums)-1)]) and len(set(nums))==4

output=test([1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4])
print(output)

'''Given a string consisting of whitespace and groups of matched parentheses, 
write a Python program to split it into groups of perfectly matched parentheses 
without any whitespace.'''

def test(str):
    ls =[]
    s2=""

    for s in str.replace(' ',''):
        s2=s2+s
        if s2.count("(") == s2.count(")"):
            ls.append(s2)
            s2= ""
    return ls

t1=test('( ()) ((()()())) (()) ()')
print(t1)

#Write a Python program to find the indexes of numbers of a given list below a given threshold.
thresh=100
def test(nums):
    for index,i in enumerate(nums):
        if i <thresh:
            print(index,end=' ')

t=test([0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55])
print(t)

#another easy way
def test(nums,n):
    return [i for i,n in enumerate(nums) if n<thresh]

nums=[0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55]
print(test(nums, thresh))


