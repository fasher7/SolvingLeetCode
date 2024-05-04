from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        count = len(strs)
        max_length = max(len(sublist) for sublist in strs)
        for x in range(max_length):
            counter = 0
            for y in range(len(strs)):
                if len(strs[y]) - 1 < x or len(strs[y]) == 0:
                    break
                if counter == 0:
                    word = strs[y][x]
                if word != strs[y][x]:
                    break
                counter += 1
            if counter == count:
                common += strs[y][x]
            else:
                break
        return common

lcp = Solution()
print(lcp.longestCommonPrefix(["flower",
                               "flow",
                               "flight"]))