class Solution:
    # lint 075
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if self.is_top(mid, arr) == -1:
                right = mid
            elif self.is_top(mid, arr) == 1:
                left = mid
            else:
                return mid
        return left if self.is_top(left, arr) == 0 else right

    def is_top(self, i, arr):
        if i + 1 == len(arr) or \
            (i + 1 < len(arr) and arr[i] > arr[i + 1]):
            return -1
        elif i == 0 or (i + 1 < len(arr) and arr[i] < arr[i + 1]):
            return 1
        else:
            return 0