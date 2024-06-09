from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] = counter[num] + 1
            else:
                counter.update({num: 1})
        maxKey, maxCount = max(counter.items(), key=lambda item: item[1])
        if maxCount >= int(len(nums)/2):
            return maxKey
    
nums = [1,2,2,1,1,2,2,3,2]
me = Solution()
print(me.majorityElement(nums))