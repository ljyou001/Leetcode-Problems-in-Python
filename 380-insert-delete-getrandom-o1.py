class RandomizedSet:
    def __init__(self):
        self.nums, self.indexes = [], {}

    def insert(self, val: int) -> bool:
        if val in self.indexes:
            return False
        self.nums.append(val)
        self.indexes[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indexes:
            return False
        index = self.indexes[val]
        last = self.nums[-1]
        last_index = len(self.nums) - 1

        self.indexes[last] = index
        self.nums[index] = last
        
        del self.indexes[val]
        self.nums.pop()
        return True       

    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()