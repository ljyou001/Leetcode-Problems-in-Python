class Solution:
    def rob(self, nums: List[int]) -> int:
        n1 = 0
        n2 = nums[0]
        
        if len(nums) == 1:
            return nums[0]

        for i in range(1, len(nums)):
            old_n2 = n2
            n2 = max(n1 + nums[i], n2)
            n1 = old_n2

        return n2