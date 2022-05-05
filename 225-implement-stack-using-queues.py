class MyStack:
    list = []
    
    def __init__(self):
        self.list=[]

    def push(self, x: int) -> None:
        self.list.append(x)

    def pop(self) -> int:
        val = self.list[-1]
        self.list = self.list[0:-1]
        return val

    def top(self) -> int:
        return self.list[-1]

    def empty(self) -> bool:
        return len(self.list) <= 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()