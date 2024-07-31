## int array num

## return an array answer

## answer[i] ==> product of all elements of nums except nums[i]

## can not use division operation 
## must be in O(n)

## avoid doing the same multiplications several times

## store the results of past multiplications in a dict
## [1, 2, 3, 4]

## answer[0] --> results of sub array before * sub array after
#### in this case no sub array after, so default to 1
#### store the result of product 
## answer[1] --> 


## answer [0] --> 1 * answer[:-1]
## answer [-1] --> 1 * answer[0:-2]
#### these would already contain many multiplications, so those would have to be done first.  
#### dict[0]= nums[0]
#### dict[1]= nums[1] * nums [2]

## 2 dicts, pre and post



### Other approach ###
### Loop through once, multiply everything.  Loop through a second time, subtract nums[i] - 1 * total

### can be solved in O(1)


### approach 3 use bit operators
    ## multiply the values of of pre * post
    ## the index of pre i - 1, index of post i + 1
    ## deal with 1st and last items 
from collections import defaultdict



def productExceptSelf(nums: list[int]) -> list[int]:
    prefix: defaultdict = defaultdict(int)  ## starting from 0, this shows the product of all preceeding items
    postfix: defaultdict = defaultdict(int) ## starting from the end, shows the product of all subsequent items
    res: list[int] = []
    
    for i, _ in enumerate(nums):
        ## prefix start from beginning
        n: int = len(nums) - 1 - i ## starts at last item in the array and decrements
        print("n", n)
        if i == 0:
            prefix[0] = nums[0] 
            postfix[n] = nums[n]
        else:
            prefix[i] = prefix[i-1] * nums[i]
            postfix[n] = postfix[n+1] * nums[n]

    for i in range(len(nums)):
        if i == 0:
            answer: int = postfix[i+1]
        elif i == len(nums) - 1:
            answer: int = prefix[i-1]
        else:
            answer: int = prefix[i - 1] * postfix[i + 1]
        res.append(answer)
    
    return res

    ### better solution
    
    # def productExceptSelf(nums: list[int]) -> list[int]:
    #     res = [1] * (len(nums))
    #     prefix = 1
        
    #     for i in range(len(nums)):
    #         res[i] = prefix
    #         prefix *= nums[i]
    #     postfix = 1
    #     for i in range(len(nums) - 1, -1, -1):
    #         res[i] *= postfix
    #         postfix *= nums[i]
    #     return res
    
    
print("RESULTS")
print(productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])