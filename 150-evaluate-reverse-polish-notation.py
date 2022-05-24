class Solution_stack:
    # a typical stack implementation
    # time: O(n)
    # space: O(n)
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2) + int(num1))
                # due to the stack's property, always start with num2 then num1
            elif i == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2) - int(num1))
            elif i == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2) * int(num1))
            elif i == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                divid = int(num2) // int(num1)
                if divid < 0 and int(num2) % int(num1) != 0:
                    divid += 1
                stack.append(divid)
            else:
                stack.append(i)
        return stack[-1]