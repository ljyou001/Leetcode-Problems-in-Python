class SolutionWithPop:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        nums_length = len(nums)
        while i < nums_length - 1:
            while i < nums_length - 1 and nums[i] == nums[i + 1]:
                a = nums.pop(i)
                nums_length = len(nums)
            i += 1
        return len(nums)

class SolutionInPlaceReplace:
    """
    If nums need to be returned, you need to trim the length of nums
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        prev = nums[0]
        res = 1
        for num in nums:
            if num == prev:
                continue
            prev = num
            nums[res] = num
            res += 1
        return res

