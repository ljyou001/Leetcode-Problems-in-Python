#!! mono increase stack

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]
        
        stack = [(heights[0],0)]
        res = len(heights) * min(heights)
        
        for i in range(1, len(heights)):
            if len(stack) == 0 or heights[i] >= stack[-1][0]:
                stack.append((heights[i],i))
            else:
                while stack and stack[-1][0] >= heights[i]:
                    height, index = stack.pop()
                    area = height * (i - index)
                    # since the index is stored in the stack, just calculate the area when pop
                    res = max(res, area)
                stack.append((heights[i], index))
        
        # dealing those areas that can extend to the end of the list
        for i in range(len(stack)):
            height, index = stack[i]
            area = height * (len(heights)-index)
            res = max(res, area)
        
        return res
    
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = [] #[[index, height],...]

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                area = (i - index) * height
                res = max(res, area)
                start = index
            stack.append([start, h])

        for i, h in stack:
            area = (len(heights) - i ) * h
            res = max(res, area)
        
        return res