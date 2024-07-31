
## array sorted in increasing order
## find first and last index of a target value, can be several of the same values
## if target is not found return [-1, -1]
## normal binary search to find first value.  When first 
## they are consecutive so only need to keep track of lowest and highest
## start at highest index / 2 to get the mid point
## 2 binary searches
    ## first one we are looking for min_v, which has target at i and lower value at -1 
    ## 2nd one looking for max_v that has target at i and higher value at +1
def searchRange(nums: list[int], target: int) -> list[int]:
    
    if nums == []:
        return [-1, -1]
    if len(nums) == 1:
        if nums[0] == target:
            return [0, 0]
        return [-1, -1]
    min_v: int = -1
    max_v: int = -1
    st: int = 0
    ed: int = len(nums) - 1
    st_next: int = 0
    ed_next: int = len(nums) - 1
    while st <= ed:
        md: int = ((ed - st) // 2) + st
        if len(nums[st:ed]) == 1:
            if nums[st] == target:
                min_v = st
                break
            elif nums[ed] == target:
                min_v = ed
                break
            else:
                return [-1, -1]
        if nums[md] == target:
            if md == 0:
                min_v = md
                break
            if nums[md - 1] < target:
                min_v = md
                break
        if nums[st] <= target <= nums[md]:
            ed = md
        elif nums[md] <= target <= nums[ed]:
            st_next = st = md
        else:
            return [-1,-1]
        
    st: int = st_next
    ed: int = len(nums) - 1
    while st <= ed:
        print(nums[st:ed])

        md: int = ((ed - st)// 2) + st
        if len(nums[st:ed]) == 1:
            if nums[ed] == target:
                max_v = len(nums) - 1
                break
            elif nums[ed-1] == target:
                if nums[ed] >= nums[ed-1]:
                    max_v = ed-1
                    break
            else:
                return [-1, -1]
        if nums[md] == target:
            if md == [len(nums)-1]:
                max_v = md
                break
            if nums[md + 1] > target:
                max_v = md
                break
        if nums[md] <= target <= nums[ed]:
            st = md
        else:
            ed = md
    return [min_v, max_v]
print("START I")
print(searchRange([1,2,3], 3), [2, 2])
print("$$$$$$$$$$$$$$$$$$\n")

print("START II")
print(searchRange([1,4], 4), [1, 1])
print("$$$$$$$$$$$$$$$$$$\n")

print("START III")
print(searchRange([1,3], 1), [0, 0])
print("$$$$$$$$$$$$$$$$$$\n")
print(searchRange([5,7,7,8,8,10], 6), [-1, -1])
print("$$$$$$$$$$$$$$$$$$\n")
print(searchRange([], 6), [-1, -1])
print("$$$$$$$$$$$$$$$$$$\n")
print(searchRange([0,0,1,1,1,2,4,4,4,4,5,5,5,6,8,8,9,9,10,10,10], 8), [14, 15])
print("$$$$$$$$$$$$$$$$$$\n")
