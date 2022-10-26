class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ''
        count, j = 0, 0
        for i in s:
            if j < len(spaces) and count == spaces[j]:
                res += " "
                j += 1
            res += i
            count += 1
            
        return res