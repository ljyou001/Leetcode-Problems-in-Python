class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives, negatives = deque(), deque()
        for i in nums:
            if i > 0:
                positives.append(i)
            else:
                negatives.append(i)
        
        is_positive = True
        res = []
        while positives or negatives:
            if is_positive:
                res.append(positives.popleft())
            else:
                res.append(negatives.popleft())
            is_positive = not is_positive
        return res

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives, negatives = [], []
        for i in nums:
            if i > 0:
                positives.append(i)
            else:
                negatives.append(i)
        
        res = []
        for i in range(len(positives)):
            res.append(positives[i])
            res.append(negatives[i])
        return res