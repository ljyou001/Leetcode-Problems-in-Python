class Solution_slow:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        res = 0
        
        while i < len(height) - 1:
            j = i + 1
            while j < len(height):
                h = min(height[i], height[j])
                res = max(res, (h * (j-i)))
                j += 1
            i += 1
            
        return res

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        res = 0
        
        while i < j:
            w = j - i
            if height[i] < height[j]:
                h = height[i]
                i += 1
            else:
                h = height[j]
                j -= 1
            res = max(res, w*h)
            
        return res