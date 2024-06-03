class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = []

    def push(self, val: int) -> None:
        if not self.min_val:
            self.min_val.append(0)
        else:
            self.min_val.append(len(self.stack) \
                           if val < self.stack[self.min_val[-1]] \
                           else self.min_val[-1])
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_val.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.min_val[-1]]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()