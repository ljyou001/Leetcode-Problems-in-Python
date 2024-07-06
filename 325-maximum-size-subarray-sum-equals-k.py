# LINT 911

class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def max_sub_array_len(self, nums: List[int], k: int) -> int:
        # Write your code here
        prefix_sum = 0
        count = {0: -1}
        res = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum - k in count:
                res = max(i - count[prefix_sum - k], res)
            if prefix_sum not in count:
                count[prefix_sum] = i
        return res