class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in logs:
            if i == '../':
                if len(stack) > 0:
                    stack.pop()
            elif i == './':
                continue
            else:
                stack.append(i)
        return len(stack)

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        num = 0
        for i in logs:
            if i == '../':
                if num > 0:
                    num -= 1
            elif i == './':
                continue
            else:
                num += 1
        return num