
def removeDuplicates(nums: list[int]) -> int:
    ## loop through the list
    ## check if number is last number checked, if it is not append to new list, if it is increase blanks counter
    ## need to modify nums
    last_number_checked: int = None
    new_list: list = []
    for num in nums:
        if num == last_number_checked:
            pass
        else

    return len(num)

removeDuplicates([1,1,2])


"""

Modify array in place

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j"""