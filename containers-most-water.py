## find the largest container.
## left = left index
## right = right index
## Max amount of water = right - left * min (array[left], array[right])
## max amount of water = width * height
## create a hash table with index, height
## store value of max water
## Iterate through the keys
from collections import defaultdict


height = [1,8,6,2,5,4,8,3,7]


class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_water_seen = 0
        left = 0
        right = len(height) - 1
        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
            max_water_seen = max(max_water_seen, current_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        print(max_water_seen)
        return max_water_seen



solution = Solution()
solution.maxArea(height)