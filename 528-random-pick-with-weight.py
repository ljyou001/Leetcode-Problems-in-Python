class Solution:

    def __init__(self, w: List[int]):
        self.weights = []
        total = 0
        for weight in w:
            total += weight
            self.weights.append(total)

    def pickIndex(self) -> int:
        random_val = random.randint(0, self.weights[-1] - 1)
        left = 0 
        right = len(self.weights) - 1
        while left < right:
            mid = (left + right) // 2
            if self.weights[mid] > random_val:
                right = mid
            else:
                left = mid + 1
        return left

        # ?
        # while left + 1 < right:
        #     mid = (left + right) // 2
        #     if self.weights[mid] > random_val:
        #         right = mid
        #     else:
        #         left = mid
        # if self.weights[left] >= random_val:
        #     return left
        # return right


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()