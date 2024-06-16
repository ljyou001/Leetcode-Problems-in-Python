class TwoSumMoreFind:
    """
    A Two pointer Exercise
    This solution is best for cases with more find call or evenly distrubution
    """
    def __init__(self):
        self.nums = []
    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        # methods:
        # A. binary search to insert? No -> this is logN+N, since you need to 
        # move the elements afterwards.
        # B. append and exchange? Yes -> O(N) -> insertion sort
        self.nums.append(number)
        index = len(self.nums) - 1
        while True:
            if index - 1 < 0 or self.nums[index - 1] <= self.nums[index]:
                break
            self.nums[index], self.nums[index - 1] = \
            self.nums[index - 1], self.nums[index]
            index -= 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        i = 0
        j = len(self.nums) - 1
        while i < j:
            if self.nums[i] + self.nums[j] == value:
                return True
            elif self.nums[i] + self.nums[j] > value:
                j -= 1
            else:
                i += 1
        return False 

class TwoSumMoreAdd:
    """
    A Two pointer exercise
    If more Add calls
    """
    def __init__(self):
        self.nums = []
    
    def add(self, number):
        self.nums.append(number)

    def find(self, value):
        self.nums.sort()
        i = 0
        j = len(self.nums) - 1
        while i < j:
            if self.nums[i] + self.nums[j] == value:
                return True
            elif self.nums[i] + self.nums[j] > value:
                j -= 1
            else:
                i += 1
            
        return False 

class TwoSumHashTable:
    """
    Hash table method
    Require extra memory
    """
    def __init__(self):
        self.counter = {}
    
    def add(self, number):
        self.counter[number] = self.counter.get(number, 0) + 1

    def find(self, value):
        for ind, val in self.counter.items():
            if value != ind + ind and self.counter.get(value - ind):
                return True
            elif value == ind + ind and self.counter.get(ind) >= 2:
                return True
        return False