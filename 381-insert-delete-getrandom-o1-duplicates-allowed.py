# LINT 954
# the question on leetcode requires a return value for each operation

class RandomizedCollection:
    def __init__(self):
        self.nums = []
        self.mapping = {}

    def insert(self, val):
        index = len(self.nums)
        self.nums.append(val)
        if self.mapping.get(val):
            # To handle `val in self.mapping` and `self.mapping[val]` has value
            self.mapping[val].add(index)
            return False
        self.mapping[val] = set([index])
        return True

    def remove(self, val):
        if not self.mapping.get(val):
            # To handle `val in self.mapping` and `self.mapping[val]` has value
            return False

        last_val = self.nums[-1]
        last_index = len(self.nums) - 1
        if val == last_val:
            # You must manually handle the case that index to remove is the last index
            self.nums.pop()
            self.mapping[val].remove(last_index)
            return True

        index = self.mapping[val].pop()
        self.mapping[last_val].remove(last_index)
        self.mapping[last_val].add(index)
        self.nums[index] = self.nums[last_index]
        self.nums.pop()
        return True

    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums) - 1)]




# class RandomizedCollection:

#     def __init__(self):
#         self.nums, self.indexes = [], {}

#     def insert(self, val: int) -> bool:
#         not_present = False
#         self.nums.append(val)
#         index = len(self.nums) - 1
#         if self.indexes.get(val):
#             self.indexes[val].add(index)
#         else:
#             not_present = True
#             self.indexes[val] = set([index])
#         return not_present

#     def remove(self, val: int) -> bool:
#         if not self.indexes.get(val):
#             return False

#         index = self.indexes[val].pop()
#         if index == len(self.nums) - 1:
#             self.nums.pop()
#             return True

#         last_val = self.nums[-1]
#         last_ind = len(self.nums) - 1
        
#         self.indexes[last_val].discard(last_ind)
#         self.indexes[last_val].add(index)
#         self.nums[index] = last_val

#         self.nums.pop()
#         return True

#     def getRandom(self) -> int:
#         return self.nums[random.randint(0, len(self.nums) - 1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()