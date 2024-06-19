from typing import (
    List,
)

class Solution:
    """
    @param a: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    # leet 658
    def k_closest_numbers(self, a: List[int], target: int, k: int) -> List[int]:
        if k == 0:
            return []
        left = right = self.binary_search_nearest(a, target)
        res = [a[left]]
        for _ in range(k - 1):
            if self.is_left_closer(a, left, right, target) == 'left':
                left -= 1
                res.append(a[left])
            else:
                right += 1
                res.append(a[right])
        return res

    def binary_search_nearest(self, arr, target):
        left = 0
        right = len(arr) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid
            else:
                right = mid
        return left if abs(target - arr[left]) <= abs(arr[right] - target)\
                else right
                # You need to use <= to enforce left, not <.

    def is_left_closer(self, arr, left, right, target):
        if left > 0 and right < len(arr) - 1:
            if abs(arr[left - 1] - target) <= abs(arr[right + 1] - target):
                return 'left'
            else:
                return 'right'
        elif left > 0:
            return 'left'
        else:
            return 'right'