class SolutionWorst:
    def leftmost_smaller(self, nums: List[int]) -> List[int]:
        # write your code here
        if not nums:
            return []
        res = []
        for i in range(len(nums)):
            res.append(self.find_leftmost_smaller(nums, i))
        return res

    def find_leftmost_smaller(self, nums, index):
        left = 0
        while left < index:
            if nums[left] < nums[index]:
                return nums[left]
            left += 1
        return -1

