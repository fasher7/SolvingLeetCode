from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if len(nums) == 0:
            return 0
        
        l = 0
        r = len(nums) - 1
        if target < nums[l]:
            return 0
        if target > nums[r]:
            return r+1

        while(True):
            m1 = l + (r-l)//3
            m2 = r - (r-l)//3

            if target == nums[m1]:
                return m1
            if target == nums[m2]:
                return m2
            
            if target < nums[m1]:
                r = m1-1
            elif target > nums[m2]:
                l = m2+1
                if l > r:
                    return r+1
            else:
                l = m1+1
                r = m2-1
                if l == r:
                    if target > nums[l]:
                        return l+1
                    else:
                        return l
                elif l>r:
                    return r+1

si = Solution()
print(si.searchInsert([1,3,5,7,9,11,12,15], 8))