#leetcode python questions

l=[0,1,0,13,12]
lst=[]
lst1=[]
for i in l:
    if i == 0:
        lst.append(i)
    else:
        lst1.append(i)
print(sorted(lst1)+lst)

pre=0
for i in range(0,len(l)):
    if l[i] !=0:
        hold=l[pre]
        l[pre]=l[i]
        l[i]=hold
        pre+=1

l=[-1,0,1,2,-1,-4]
lst=[]
lst1=[]
for i in l:
    for j in l:
        for k in l:
            if i != k and j != i and k!= i and j!= k and i+j+k==0:
                if [i,j,k] not in lst:
                   lst1.append([i,j,k])
                   print(i,j,k)
print(lst1)
res=[]
for i in range(len(l)):
    for j in range(len(l)):
        for k in range(len(l)):
            if l[i] !=l[j] and l[k]!=l[i] and l[j]!=l[k] and l[i]+l[j]+l[k]==0:
                res.append(sorted([l[i],l[j],l[k]]))
                print(l[i],l[j],l[k])
print(res)


# return a list of lists of length 3
def three_Sum(num):
    if len(num) < 3: return []
    num.sort()
    result = []
    for i in range(len(num) - 2):
        left = i + 1
        right = len(num) - 1
        if i != 0 and num[i] == num[i - 1]: continue
        while left < right:
            if num[left] + num[right] == -num[i]:
                result.append([num[i], num[left], num[right]])
                left = left + 1
                right = right - 1
                while num[left] == num[left - 1] and left < right: left = left + 1
                while num[right] == num[right + 1] and left < right: right = right - 1
            elif num[left] + num[right] < -num[i]:
                left = left + 1
            else:
                right = right - 1
    return result


nums1 = [-1, 0, 1, 2, -1, -4]
nums2 = [-25, -10, -7, -3, 2, 4, 8, 10]
print(three_Sum(nums1))
print(three_Sum(nums2))



ls= [-1, 0, 1, 2, -1, -4]
res=[]
ls.sort()
length=len(ls)
for i in range(length-2):
    if i>0 and ls[i]==ls[i-1]:
        continue
    l=i+1
    r=length-1

    while l<r:
        total=ls[i]+ls[l]+ls[r]
        if total<0:
            l=l+1
        elif total >0:
            r=r-1
        else:
            res.append([ls[i],ls[l],ls[r]])
            while l<r and ls[l]==ls[l+1]:
                l=l+1
            while l<r and ls[r]==ls[r-1]:
                r=r-1
            l=l+1
            r=r-1
print(res)


s='abcabcbb'
map={}
max_len=start=0

for i in range(len(s)):
    if s[i] in map and start <=map[s[i]]:
        start=map[s[i]]+1
    else:
        max_len=max(max_len,i-start+1)
    map[s[i]] =i
print(max_len)

s='IX'
dic={'I':1,'V':5,'X':10,'L':50,'C':100,'M':1000}
cur=0
pre=0
tot=0
for i in range(len(s)):
    cur=dic[s[i]]
    if cur>pre:
        tot=tot+cur -2*pre
    else:
        tot+=cur
    pre=cur
print(tot)
