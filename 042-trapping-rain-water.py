class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        i = 0
        j = len(height) - 1
        ml = height[0]
        mr = height[len(height) - 1]
        res = 0
        
        while i <= j:
            if ml < mr:
                ml = max(ml, height[i])
                res += ml - height[i]
                i += 1
                
            if ml >= mr:
                mr = max(mr, height[j])
                res += mr - height[j]
                j -= 1
                
        return res
    
class MaxMinArrayMethod:
    
    def trap(self, height: List[int]) -> int:
        import copy
        if len(height) < 3:
            return 0

        max_left = copy.deepcopy(height)
        for i in range(1, len(max_left)):
            if max_left[i] < max_left[i - 1]:
                max_left[i] = max_left[i - 1]
        
        max_right = copy.deepcopy(height)
        for i in range(len(height) - 2, -1, -1):
            if max_right[i] < max_right[i + 1]:
                max_right[i] = max_right[i + 1]
        
        min_lr = [0] * len(height)
        for i in range(len(min_lr)):
            min_lr[i] = min(max_left[i], max_right[i])

        res = 0
        for i in range(len(height)):
            res += min_lr[i] - height[i] if min_lr[i] - height[i] > 0 else 0
        
        return res