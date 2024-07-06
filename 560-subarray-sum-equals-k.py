class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = {0: 1}
        res = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum - k in count:
                res += count[prefix_sum - k]
            count[prefix_sum] = count.get(prefix_sum, 0) + 1
        return res

# THINK: Why need to use count hashtable rather than a set?

# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix_sum = [0]
        # for i in range(len(nums)):
        #     prefix_sum.append(prefix_sum[i] + nums[i])
        # prefix_sum_set = set(prefix_sum)
        # res = 0
        # for i in range(len(prefix_sum)):
        #     if prefix_sum[i] - k in prefix_sum_set:
        #         res += 1
        # return res