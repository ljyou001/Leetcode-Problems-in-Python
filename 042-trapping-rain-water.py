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