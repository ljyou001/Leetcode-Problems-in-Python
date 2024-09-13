class Solution:
    def calculate(self, s: str) -> int:
        NUMBER = set('0123456789')
        stack = []
        
        i = 0
        num = 0
        sign = '+'
        while i < len(s):
            if s[i] in NUMBER:
                num = num * 10 + int(s[i])
            if s[i] in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] *= num
                elif sign == '/':
                    stack[-1] = int(stack[-1] / num)
                sign = s[i]
                num = 0
            i += 1
        res = 0
        while stack:
            res += stack.pop()

        return res