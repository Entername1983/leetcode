# array in ascending order that is rotated beteween 1 and n times.
# elements are unique
# rotating the array means putting the last item in teh first position
# 0 1 2 4 5 6 7 
# 7 0 1 2 4 5 6
# 6 7 0 1 2 4 5
# 5 6 7 0 1 2 4
# 4 5 6 7 0 1 2
# if we know how many times it was rotated, we can reconstruct the array original array

# orig_array = sub_rotated_array[n:-1] + sub_rotated_array[0:n-1]
## but we dont know how many time is was rotates

## if we find a number and the following number is smaller, then that is the lowest.  Smallest number will always be preceded by a larger number (unless its the first)
## conduct a binary search, check if number directly below mid is less, if so return mid.  

## Can we use the length of the array ? Not useful

## if the sub array is ascending, we can adjust points accordingly 
## if the sub array is ascending, we know that the target has to be st or less 



def findMin(nums: list[int]) -> int:
    ## reconstruct original array
    if len(nums) == 1:
        return nums[0]
    st: int = 0
    ed: int = len(nums) - 1
    min_v: int = None
    while st <= ed:
        md: int = (( ed - st ) // 2) + st
        if md - 1 >= 0:
            if nums[md] < nums[md-1]:  ## index out of range to handle here
                return nums[md]
        if md + 1 <= len(nums) - 1:
            if nums[md] > nums[md+1]:
                return nums[md+1]  ## index out of range to handle here
        if nums[st] < nums [md]:
            ## we know that the value must be smaller or equal to nums[st], can discard the rest of the subarray:
            if min_v is None or nums[st] < min_v:
                min_v = nums[st]
            ## we should also check the other side.  
            st = md + 1
        if nums[md] < nums[ed]: ## we know the value is must be 
            if min_v is None or nums[md] < min_v  :
                min_v = nums[st]
            ed = md - 1
    return min_v
                
        ## how to decide which side to shift?
        ## use recursion?
        
print("RESULTS")
print(findMin(nums = [1]), "1")

print(findMin(nums = [3, 4, 5, 1, 2]), "1")
print(findMin(nums = [4, 5, 6, 7, 0, 1, 2]), "0")
print(findMin(nums = [11, 13, 15, 17]), "11")
