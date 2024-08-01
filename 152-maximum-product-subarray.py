class SolutionBasicIterDP:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max = [1] * (len(nums) + 1)
        dp_min = [1] * (len(nums) + 1)
        res = float('-inf')
        for i in range(1, len(nums) + 1):
            if nums[i - 1] == 0:
                dp_max[i] = 0
                dp_min[i] = 0
                res = max(dp_max[i], res)
                continue
            dp_max[i] = max(
                nums[i - 1] * dp_max[i - 1],
                nums[i - 1] * dp_min[i - 1],
                nums[i - 1]
            )
            dp_min[i] = min(
                nums[i - 1] * dp_max[i - 1],
                nums[i - 1] * dp_min[i - 1],
                nums[i - 1]
            )
            res = max(dp_max[i], res)
        return res

class SolutionIterDPRollingArray:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = cur_min = res = nums[0]
        for num in nums[1:]:
            if num == 0:
                res = max(res, 0)
                cur_max = cur_min = 1
                continue
            prev_max = cur_max
            # for cur_min calculation, otherwise cur_max calculation will affect
            cur_max = max(
                num * cur_max,
                num * cur_min,
                num,
            )
            cur_min = min(
                num * prev_max,
                num * cur_min,
                num,
            )
            res = max(res, cur_max)
        return res