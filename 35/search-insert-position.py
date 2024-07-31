
## sorted array of distinct integers
## if target is found return the index
## else return index where it would be inserted
## needs to be O(log n)
## will need to use binary search
## take the array, find middle point.  If target = middle point --> return the index
## if target is higher, find middle point, if target == middle point --> return the index
## if target is lower, find the middle point if target == middle point --> return the index

## could check if target is in the remaining array
## this wont work as no way to keep track of middle point
def searchInsert(nums: list[int], target: int) -> int:
    print(f"target {target}")
    start = 0
    end = None
    while True:
        array = nums[start:end]
        middle =len(array)//2
        print("new array", array, "middle point", middle + start)
        if target == nums[middle + start]:
            return middle + start
        elif target > nums[middle + start]:
            start = middle + start
        else:
            end = middle + start
        if len(array) == 1:
            if target > nums[middle + start]:
                return middle + start + 1
            else:
                return middle + start





print(searchInsert(nums=[1, 3, 5, 6], target=5) == 2)
print(searchInsert(nums=[1, 3, 5, 6], target=2) == 1)
print(searchInsert(nums=[2,7,8,9,10], target=9) == 3)