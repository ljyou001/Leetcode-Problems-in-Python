# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        peak = self.find_peak(mountain_arr)
        left_index = self.binary_search(mountain_arr, target, False, 0, peak)
        if left_index != -1:
            return left_index
        right_index = self.binary_search(mountain_arr, target, True, peak, mountain_arr.length() - 1)
        return right_index

    def binary_search(self, mountain_arr, target, desc, left, right):        
        while left <= right:
            mid = (left + right) // 2
            mid_value = mountain_arr.get(mid)
            if mid_value == target:
                return mid
            
            if not desc:
                if mid_value < target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if mid_value < target:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

    def find_peak(self, mountain_arr):
        left = 0
        right = mountain_arr.length() - 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid
            else:
                right = mid
        right_value = mountain_arr.get(right)
        left_value = mountain_arr.get(left)
        if right_value > left_value:
            return right
        return left