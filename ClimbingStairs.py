class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        
        val1 = 1
        val2 = 1
        while n != 1:
            temp = val1 + val2
            val1 = val2
            val2 = temp
            n-=1
        return temp
    
    """ 
    Note to Myself: Please go thrrough the concept of 
    Brute Force, Memoization & Dynamic Programming again
    in case you forgot how you solved it
    """
    
cs = Solution()
print(cs.climbStairs(5))