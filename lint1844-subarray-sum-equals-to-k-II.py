from typing import (
    List,
)

class Solution:
    def subarray_sum_equals_k_i_i(self, nums: List[int], k: int) -> int:
        prefix_sums = {0: -1}
        prefix_sum = 0
        res = float('inf')
        for i in range(len(nums)):
            prefix_sum += nums[i]
            prefix_sums[prefix_sum] = i
            if prefix_sum - k in prefix_sums:
                res = min(res, i - prefix_sums[prefix_sum - k])
        return res if res != float('inf') else -1
