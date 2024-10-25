class Solution:
    def minInsertions(self, s: str) -> int:
        if not s:
            return 0
        
        count = 0
        stack = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append('(')
                i += 1
            elif s[i: i + 2] == '))':
                # string slicing does not need to check i + 1 < len(s)
                if stack:
                    stack.pop()
                else:
                    count += 1
                i += 2
            else: 
            # s[i: i + 2] == ')(' or s[i: i + 2] == ')':
                if stack:
                    stack.pop()
                    count += 1
                else:
                    count += 2
                i += 1

        count += 2 * len(stack)
        return count