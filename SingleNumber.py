from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        checker = {}
        for num in nums:
            if num in checker:
                checker.pop(num)
            else:
                checker.update({num: None})
        
        return list(checker.keys())[0]
    
nums = [1,2,4,1,2]
sn = Solution()
print(sn.singleNumber(nums))