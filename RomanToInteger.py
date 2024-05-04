class Solution:
    def romanToInt(self, s: str) -> int:
        record = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s += " "
        sum = 0
        for rom in range(len(s)):
            if s[rom] in record:
                if s[rom] == "I":
                    if s[rom+1] == "V" or s[rom+1] == "X":
                        sum -= record[s[rom]]
                    else:
                        sum += record[s[rom]]
                elif s[rom] == "X":
                    if s[rom+1] == "L" or s[rom+1] == "C":
                        sum -= record[s[rom]]
                    else:
                        sum += record[s[rom]]
                elif s[rom] == "C":
                    if s[rom+1] == "D" or s[rom+1] == "M":
                        sum -= record[s[rom]]
                    else:
                        sum += record[s[rom]]
                else:
                    sum += record[s[rom]]
        return sum

s = "MCMXCIV"
rti = Solution()
print(rti.romanToInt(s))