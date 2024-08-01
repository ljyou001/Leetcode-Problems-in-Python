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