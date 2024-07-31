
## array rotated n times
## rotated means moving the last item to the first position.  
## can contain duplicates
## go through, if its ascending, then start value must be lowest possible in that sub array
##### discard sub array and move on
# [4, 0, 0, 0, 1, 2, 4]
def findMin(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    
    st: int = 0
    ed: int = len(nums) - 1 
    min_v: int = 5001 ## this is the highest possible value
    
    while st <= ed:
        md: int = ((ed - st) // 2 ) + st
        print("--------")
        print(f"st:{st} -v:{nums[st]}, ed:{ed} -v:{nums[ed]}, md:{md} -v:{nums[md]}")
        print(f"array {nums[st:ed+1]}, min_v {min_v}")
        if ed == st:
            if nums[ed] < min_v:
                min_v = nums[md]
            return min_v
        if nums[st] < nums[md]:
            ## its ascending
            if nums[st] < min_v:
                min_v = nums[st]
            st = md + 1
        if nums[st] == nums[md]:
            print("nums md = nums st")
            if nums[st] < min_v:
                min_v = nums[st]
            st += 1
        if nums[md] < nums[ed]:
            if nums[md] < min_v:
                min_v = nums[md]
            ed = md - 1
        if nums[md] == nums[ed]:
            if nums[ed] < min_v:
                min_v = nums[ed]
            ed -= 1

    return min_v
    
    
    
# class Solution:
#     def findMin(self, nums: list[int]) -> int:
#         start, end = 0, len(nums) - 1

#         while start < end:
#             mid = (start + end) // 2

#             if nums[mid] > nums[end]:
#                 start = mid + 1
#             elif nums[mid] < nums[start]:
#                 end = mid
#             else:
#                 end -= 1

#         return nums[start]
    
    
    
print("RESULTS")
print(findMin(nums = [1, 1]), "1")
print(findMin(nums = [3, 1]), "1")
print(findMin(nums = [1]), "1")
print(findMin(nums = [1,3,5]), "1")
print(findMin(nums = [4, 5, 6, 7, 0, 1, 2]), "0")
print(findMin(nums = [2,2,2,0,1]), "0")
