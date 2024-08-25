class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return ''

        s = list(s)
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(('(', i))
            elif s[i] == ')':
                if stack and stack[-1][0] == '(':
                    stack.pop()
                else:
                    stack.append((')', i))
            else:
                pass

        res = ''
        j = 0
        for i in range(len(s)):
            if j < len(stack) and i == stack[j][1]:
                j += 1
                continue
            res += s[i]

        return res