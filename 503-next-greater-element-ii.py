class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        length = len(nums)
        nums += nums[:]
        stack = []
        res = [-1] * length
        for i in range(len(nums)):
            while stack and nums[i] > stack[-1][1]:
                index, val = stack.pop()
                if index < length:
                    res[index] = nums[i]
            stack.append((i, nums[i]))
        return res