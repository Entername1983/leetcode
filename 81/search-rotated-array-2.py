



# array, that was increasing, but part of it is flipped
# not necessarily distinct values
# because of that we can find 2 halfs that are both increasing
# that woudl only be true if the end points are the same?? NO
# if they are both increasing did we hit the pivot point as m?
# can a sub array be increasing and have a lower number in it?  <-- This should not be possible.  
# can check if a sub array is increasing, check if the target is lower than mid

def search(nums: list[int], target: int) -> bool:


    st: int = 0
    ed: int = len(nums) - 1
    i = 0
    while st <= ed:
        i += 1
        md: int = ((ed - st)// 2) + st
        print(f"st:{st} --> {nums[st]}, ed:{ed} --> {nums[ed]}, md:{md} -->", nums[md])
        print("array", nums[st:ed+1])
        # if nums[st] == nums[md] == nums[ed]:  ## this edge case becomes an issue.  Can either recursively search through it or just loop through all values.  
        #      ## will try looping through all values even though 
        #      st += 1
        #      ed += 1
            

        if nums[md]  == target or nums[st]  == target or nums[ed] == target:
            print("!!!!!!")
            return True
        
        if nums[st] < nums[md]:
            ## the sub array is increasing --> check if target is lower.  
            # if its icnreasing, it has to be between 2 values
            # If target is lower than nums[st] then it is not in this sub array
            if nums[st] < target < nums[md]:
                ed = md 
            else:
                 st = md
        elif nums[st] == nums[md]:
            print("shortening array from left")
            st += 1
        if nums[md] < nums[ed]:
            if nums[md] < target < nums[st]:
                    st = md   
            else:
                 ed = md    
        elif nums[md] == nums[ed]:
             print("shortening array from right")
             ## we know md is not the value and so we know ed is not the value.  So we can reduce ed by one
             ed -= 1
        if i == 10:
            break
    print("___________")

    return False







print("RESULTS")
# print(search(nums = [1,0,1,1,1], target = 0), 'True')
# print(search(nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], target = 2), 'True')
# print(search(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2], target = 1), 'True')
# print(search(nums = [2, 5, 6, 0, 0, 1, 2], target = 0), 'True')
# print(search(nums = [2, 5, 6, -1, 2], target = 3), 'False')
# print(search(nums = [2], target = 0), 'False')
# print(search(nums = [2], target = 2), 'True')
print(search(nums = [3,4,4,4,4,4,4,5,5,6,6,6,6,6,6,6,7,7,7,7,7,7,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,10,10,10,-10,-10,-10,-9,-8,-8,-8,-8,-8,-7,-7,-7,-7,-6,-6,-6,-6,-6,-6,-6,-5,-5,-5,-4,-4,-4,-4,-3,-3,-3,-3,-3,-3,-2,-2,-2,-2,-1,-1,0,0,0,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3], target = 2), 'True')