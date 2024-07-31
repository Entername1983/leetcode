## numbers is ascending
## find 2 numbers, 2nd number rgheater than the otehr such that they add up to target
## have a left and right pointer
## if sum of both is greater 
## start in the middle.  If sum is too high, move left to the left.  Do so until reaching lowest index, if still too high move right one left
## do the opposite if sum is too low

## 1, 2, 3, 5, 6, 9, 10, 12, 16, 20.    target 5
## will work but too inefficient

## could start at index 0, loop through and do a binary search at each index to find a target.
## should also work, not most efficient


## what we know:
#### always minimum 2 items in numbers
#### left + right == target so left == target - right 
#### left < right 
#### only one solution possible
#### numbers can be negative


def twoSum(numbers: list[int], target: int) -> list[int]:
    
    for i, value in enumerate(numbers):
        st: int = i + 1
        ed: int = len(numbers) - 1
        count = 0
        while st <= ed:
            count += 1
            md: int = ((st-ed)//2) + st
            print(f"i {i}, value {value}, st {st}, ed {ed}, md {md}")

            temp_t = target - numbers[md]
            print("tempt", temp_t)
            if i != md:
                if value == temp_t:
                    return [i + 1, md + 1]
            if value == numbers[st]:
                return [i + 1, st + 1]
            if temp_t > numbers[ed]:
                break
            if numbers[st] <= temp_t <= numbers[md]:
                print("here")
                ed -= 1
            if numbers[md] <= temp_t <= numbers[ed]:
                st += 1
            if count == 4:
                break
        return [-1, -1]
print(twoSum([0,0,3,4]
, 0))
# print(twoSum([2,3,4], 6))