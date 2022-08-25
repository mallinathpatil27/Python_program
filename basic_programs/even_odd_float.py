#to check the even or odd for  float values

def solve(n):
    s = str(n)    #im taking 100.70 value here its length is 6 including dot 
    flag = False   # to the dot symbol we can take the boolen expression
    for i in range(len(s) - 1, -1, -1):   # iterating in reverse order from suppose len is 6 including dot symbol(i.e 100.70) then it start from last i.e 6-1
        if s[i] == '0' and flag == False:  # if s[5] i e 0 if it is true it will go back and continue the  next iteration
            continue

        if s[i] == '.':
            flag = True
            continue

        if int(s[i]) % 2 == 0:
            return "Even"

        return "Odd"

n = 100.70
print(solve(n))
