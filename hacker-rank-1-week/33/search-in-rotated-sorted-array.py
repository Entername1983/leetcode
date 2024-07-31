"""There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 
 Input: nums = [4,5,6,7,8,9,10,0,1,2,3,4,5], target = 8

 
 
 
Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
"""
## use binary search
## how do we split it up
## first need to find pivot index? 
## need to mark sections as ascending or descending
## if we find a section that is descending, we know the other side is ascneding and can perform normal binary search  [3,5,1]

def search(nums: list[int], target: int) -> int:
    ## initalize, left and right pointers
    l, r = 0, len(nums) - 1
    ## keep going until left is below right (or we found it and return)
    if len(nums) < 1:
        return -1
    while l <= r:
        if len(nums[l:r]) == 0:
            if nums[l] != target:
                return -1
            return l
        if len(nums[l:r]) == 1:
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            else:
                return -1
            
            
        m = ((r-l) // 2) + l ## midpoint
        if nums[m] == target:
            return m
        if nums[m] > nums[r]:
            if nums[l] <= target <= nums[m]:
                r = m
            else:
                l = m
        else:
            if nums[m] <= target <= nums[r]:
                l = m 
            else:
                r = m
        # else: 
        #     print("do we ever enter into this?")
        #     if target > nums[m]:
        #         l = m
        #     elif target < nums[m]:
        #         r = m
        #     elif target == nums[m]:
        #         return m
    return -1
                
# [4,5,6,7,0,1,2]
# print(search(nums= [4,5,6,7,0,1,2], target = 0), "4")
print(search(nums= [4], target = 4), "0")
print(search(nums= [4, 1], target = 1), "1")

print('-------------------------')
print(search(nums= [4,5,6,7,0,1,2], target = 3), "-1")
print('-------------------------')
print(search(nums= [3,5,1], target = 3), 0)
