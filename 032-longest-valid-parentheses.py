class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0: return 0
        res = 0
        count = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
                
        return res