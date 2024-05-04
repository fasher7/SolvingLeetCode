class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        checker = []
        for par in range(len(s)):
            if s[par] == ')':
                if len(checker) == 0:
                    return False
                top = checker[-1]
                if top != '(':
                    return False
                else:
                    checker.pop()
            elif s[par] == ']':
                if len(checker) == 0:
                    return False
                top = checker[-1]
                if top != '[':
                    return False
                else:
                    checker.pop()
            elif s[par] == '}':
                if len(checker) == 0:
                    return False
                top = checker[-1]
                if top != '{':
                    return False
                else:
                    checker.pop()
            else:
                checker.append(s[par])
        if len(checker) == 0:
            return True
        else:
            return False     
                
vp = Solution()
print(vp.isValid("){"))
