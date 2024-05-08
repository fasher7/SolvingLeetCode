from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = []       Time Limit Exceeded
        # for x in range(len(prices)):
        #     for y in range(x+1, len(prices)):
        #         if prices[y] > prices[x]:
        #             profit.append(prices[y] - prices[x])
        # if not profit:
        #     return 0
        # return max(profit)
        maxProfit = 0
        minPrice = prices[0]
        for price in prices[1:]:
            maxProfit = max(maxProfit, price - minPrice)
            minPrice = min(price, minPrice)
        return maxProfit

mp = Solution()
print(mp.maxProfit([7,1,5,3,6,4]))