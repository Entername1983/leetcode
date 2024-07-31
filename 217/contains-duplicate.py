## given an integer array nums return true of any value appears at least twice in teh array , and return false if every element is distinct
## create a hash map wiht values seen
from collections import defaultdict


def containsDuplicate(nums: list[int]) -> bool:
    
    mapping: defaultdict = defaultdict(int)
    for value in nums:
        if value in mapping:
            return True
        else:
            mapping[value] = 0
    return False

## shoudl have used a set
# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)
#         return False


print(containsDuplicate(nums=[1, 2, 3, 1]), 'true')
print(containsDuplicate(nums=[1,2,3,4]), 'false')
print(containsDuplicate(nums=[1]), 'false')
print(containsDuplicate(nums=[1, 1, 1, 1]), 'true')
print(containsDuplicate(nums=[2, 2, 3, 1]), 'true')
print(containsDuplicate(nums=[1, 2, 3, 0]), 'false')