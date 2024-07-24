def singleNumber2(nums):
    res = 0
    for num in nums:
        print("res", res, "num", num)
        res = res ^ num
        print("res", res)
    print("answer is", res)
    return res


singleNumber2([1, 2, 2, 3, 1])

