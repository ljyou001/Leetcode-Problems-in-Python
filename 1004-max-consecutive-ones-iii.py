class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        left = 0
        right = 0
        cur_zeros = 0

        while right < len(nums):
            if nums[right] == 1:
                res = max(res, (right - left) + 1)
                right += 1
                continue

            # if nums[right] == 0
            cur_zeros += 1
            while cur_zeros > k:
                if nums[left] == 0:
                    cur_zeros -= 1
                left += 1
            res = max(res, (right - left) + 1)
            right += 1
            
        return res
