from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        y = 0
        for x in range(len(nums)):
            if (x > y):
                y = x
            while y != len(nums):
                if nums[y] == 0:
                    y += 1
                    if y == len(nums):
                        break
                else:
                    if nums[x] == 0:
                        temp = nums[x]
                        nums[x] = nums[y]
                        nums[y] = temp
                    else:
                        break
        print(nums)
    
nums = [1,0]
mz = Solution()
mz.moveZeroes(nums)