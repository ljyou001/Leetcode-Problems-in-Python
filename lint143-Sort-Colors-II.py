from typing import (
    List,
)

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sort_colors2(self, colors: List[int], k: int):
        # write your code here
        self.sort_k(colors, 1, k, 0, len(colors) - 1)
    
    def sort_k(self, colors, color_from, color_to, index_from, index_to):
        if color_from == color_to or index_from == index_to:
            return

        left = index_from
        right = index_to
        pivot = (color_from + color_to) // 2
        
        while left <= right:
            while left <= right and colors[left] <= pivot:
                left += 1
            while left <= right and colors[right] > pivot:
                right -= 1
            
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                right -= 1
                left += 1
        
        self.sort_k(colors, color_from, pivot, index_from, right)
        self.sort_k(colors, pivot + 1, color_to, left, index_to)