class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        k = k % len(nums)
        nums[:] = self.rotate_list(nums)
        nums[:k] = self.rotate_list(nums[:k])
        nums[k:] = self.rotate_list(nums[k:])

    def rotate_list(self, list):
        return list[::-1]