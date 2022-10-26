class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            if i % 2 == 0:
                count[i] = count.get(i, 0) + 1
                
        if len(count) == 0:
            return -1
        
        res = 0
        count_val = 0
        for i in count:
            if count[i] > count_val:
                res = i
                count_val = count[i]
            if count[i] == count_val and res > i:
                res = i
        return res