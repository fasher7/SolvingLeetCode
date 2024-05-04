from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        finder = {}
        for x in range(len(nums)):
            remaining = target - nums[x]
            if remaining in finder:
                return [finder[remaining], x]
            finder[nums[x]] = x

nums = [11,2,7,15]
target = 9
ts = Solution()
print(ts.twoSum(nums, target))