# leet 381
# No return True/False in this question

import random

class RandomizedCollection(object):

    def __init__(self):
        self.nums = []
        self.mapping = {}

    def insert(self, val):
        if val in self.mapping:
            self.mapping[val].add(len(self.nums))
        else:
            self.mapping[val] = set([len(self.nums)])
        self.nums.append(val)

    def remove(self, val):
        if not self.mapping.get(val):
            return
        
        last_index = len(self.nums) - 1
        last_val = self.nums[last_index]
        index_to_del = self.mapping[val].pop()
        if index_to_del == last_index:
            self.nums.pop()
            return

        self.mapping[last_val].remove(last_index)
        self.mapping[last_val].add(index_to_del)
        self.nums[index_to_del] = self.nums[last_index]
        self.nums.pop()

    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums) - 1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()