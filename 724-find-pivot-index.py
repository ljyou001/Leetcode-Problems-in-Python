class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0]
        for i in range(len(nums)):
            prefix.append(prefix[i] + nums[i])
        last = prefix[len(prefix) - 1]

        for i in range(1, len(prefix)):
            if last - prefix[i] == prefix[i - 1]:
                return i - 1
        return -1