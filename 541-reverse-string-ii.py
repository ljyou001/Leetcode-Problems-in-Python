class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ''
        stack = []
        reverse = True
        length = 0
        for i in range(len(s)):
            if reverse:
                if len(stack) == k-1 or i == len(s) - 1:
                    stack.append(s[i])
                    while stack:
                        res += stack.pop()
                    reverse = False
                else: 
                    stack.append(s[i])
            else:
                if length < k-1:
                    res += s[i]
                    length += 1
                else: 
                    res += s[i]
                    reverse = True
                    length = 0
        return res