class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        numbers = '1234567890'
        stack = []
        
        for i in range(len(s)):
            if s[i] == ']':
                string = []
                number = []
                while stack[-1] != '[':
                    string.append(stack.pop())
                string = ''.join(string[::-1])
                stack.pop()
                while len(stack) > 0 and stack[-1] in numbers:
                    number.append(stack.pop())
                number = ''.join(number[::-1])
                string = string * int(number)
                stack.append(string)
            else:
                stack.append(s[i])
        
        return ''.join(stack)