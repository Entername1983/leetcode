def removeElement(nums: list[int], val: int) -> int:
    counter = 0
    for i, value in enumerate(nums):
        if value != val:
            nums[counter] = value
            counter += 1
    # not necessary
    # j = counter
    # while j < len(nums):
    #     nums[j] = "_"
    #     j += 1
    return counter


removeElement(nums = [3,2,2,3], val = 3)



# End-of-file (EOF)