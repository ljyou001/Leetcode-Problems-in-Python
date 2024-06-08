class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        if not nums:
            return []
        nums_left = []
        nums_right = []
        nums_mid = []
        for num in nums:
            if num < pivot:
                nums_left.append(num)
            elif num > pivot:
                nums_right.append(num)
            else:
                nums_mid.append(num)
        return nums_left + nums_mid + nums_right