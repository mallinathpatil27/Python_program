# recursive

def test(nums):
 for i in nums:
     if nums[i] != nums[i+1] and len(set(nums)) == 4:
         print('True')
         break
     else:
         print('False')


t=test([1, 3, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4])
print(t)
