class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = ''
        length = len(part)
        
        for i in s:
            stack += i
            if stack and stack[(length * -1):] == part:
                stack = stack[:length*-1]
        return stack