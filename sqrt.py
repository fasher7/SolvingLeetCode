class Solution:    #Accepted but very bad runtime
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1 or x == 2:
            return 1
        else:
            for y in range(1, int(x/2)+1):
                if y*y == x:
                    return y
                elif y*y > x:
                    return y-1
            return y
    
ms = Solution()
print(ms.mySqrt(24))