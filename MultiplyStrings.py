class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))

mult = Solution()
print(mult.multiply("123", "456"))