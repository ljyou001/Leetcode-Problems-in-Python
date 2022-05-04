class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_num = nums1 + nums2
        new_num = sorted(new_num)
        half = len(new_num) // 2
        avg = len(new_num) % 2
        if avg == 1:
            return new_num[half]
        else: 
            return (new_num[half] + new_num[half-1])/2
