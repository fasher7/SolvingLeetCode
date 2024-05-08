from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        outerList = []
        innerList = [1]
        outerList.append(innerList)
        if numRows == 1:
            return outerList
        for x in range(numRows-1):
            anotherList = []
            if len(innerList) == 1:
                 outerList.append([1,1])
            else:
                sum = 0
                innerList = outerList[x]
                anotherList.append(innerList[0])
                for y in range(len(innerList)-1):
                    sum = innerList[y] + innerList[y+1]
                    anotherList.append(sum)
                anotherList.append(innerList[-1])
                outerList.append(anotherList)
            innerList = []
        return outerList

pt = Solution()
print(pt.generate(7))