class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        def split(b, e):
            m = (b+e)//2
            if b > e:
                return e + 1
            if nums[m] == target:
                return m
            elif nums[m] < target:
                return split(m + 1, e)
            else:
                return split(b,m - 1 )
                
        return split(i, j)