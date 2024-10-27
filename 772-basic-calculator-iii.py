# LINT 894

OPERATORS = set('+-*/')
DIGITS = set('0123456789')

class Solution:
    def calculate(self, s: str) -> int:
        # Write your code here
        if not s:
            return 0
        
        return self.calculate_seg(s, 0)[0]

    def calculate_seg(self, s, start):
        stack = []
        i = start

        number = ''
        operator = '+'
        while i <= len(s):
            if i >= len(s) or s[i] in OPERATORS or s[i] == ')':
                if operator == '+':
                    stack.append(int(number))
                elif operator == '-':
                    stack.append(int(number) * -1)
                elif operator == '*':
                    val = stack.pop() * int(number)
                    stack.append(val)
                else: # is /
                    val = int(stack.pop() / int(number))
                    stack.append(val)
                number = ''
                operator = s[i] if i < len(s) else ''
                if i < len(s) and s[i] == ')':
                    break
            elif s[i] == '(':
                number, i = self.calculate_seg(s, i + 1)
            elif s[i] in DIGITS:
                number += s[i]
            i += 1
        return sum(stack), i
