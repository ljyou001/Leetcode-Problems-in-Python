# use while: more stable

class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if self.stack_out:
            return self.stack_out.pop()
        while self.stack_in:
            val = self.stack_in.pop()
            self.stack_out.append(val)
        return self.stack_out.pop()
        
    def peek(self) -> int:
        if self.stack_out:
            return self.stack_out[-1]
        while self.stack_in:
            val = self.stack_in.pop()
            self.stack_out.append(val)
        return self.stack_out[-1]

    def empty(self) -> bool:
        if self.stack_in or self.stack_out:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if self.stack_out:
            return self.stack_out.pop()
        for i in range(len(self.stack_in)):
            val = self.stack_in.pop()
            self.stack_out.append(val)
        return self.stack_out.pop()
        
    def peek(self) -> int:
        if self.stack_out:
            return self.stack_out[-1]
        for i in range(len(self.stack_in)):
            val = self.stack_in.pop()
            self.stack_out.append(val)
        return self.stack_out[-1]

    def empty(self) -> bool:
        if self.stack_in or self.stack_out:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()