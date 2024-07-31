# given an integer array nums and an integer k, return the k most frequent elements.
# can return the answer in any order

from collections import defaultdict


def topKFrequent(nums:list[int], k: int) -> list[int]:
    
    mapping: defaultdict = defaultdict(int)
    array = [[] for _ in range(len(nums) + 1)]
    answer = []
    
    for i, value in enumerate(nums):
        if value in mapping:
            mapping[value] += 1
        else:
            mapping[value] = 1
    
    for item in mapping.items():
        array[item[1]].append(item[0])
    
    i = len(nums)
    while i >= 1:
        answer += array[i]
        if len(answer) == k:
            return answer
        i -= 1
    
        
    # while True:
    #     # if array[len(nums)  -i] != []:
    #     answer += array[len(nums)-i]
    #     j += len(array[len(nums)-i])
    #     i += 1
    #     if j == k:
    #         return answer
    
print(topKFrequent(nums=[1, 1, 1, 2, 2, 3], k = 2), "[1, 2]")   
print(topKFrequent(nums=[1], k = 1), "[1]")   