class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = {0: 1}
        res = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            mod = prefix_sum % k
            if mod in count:
                res += count[mod]
            count[mod] = count.get(mod, 0) + 1
        return res
 