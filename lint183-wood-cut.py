from typing import (
    List,
)

class Solution:
    """
    @param l: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def wood_cut(self, l: List[int], k: int) -> int:
        if sum(l) < k:
            return 0
        left = 1
        right = max(l)
        while left + 1 < right:
            mid = (left + right) // 2
            if self.get_pieces(l, mid) < k:
                right = mid
            else:
                left = mid
        if self.get_pieces(l, right) >= k:
            return right
        return left
        
    def get_pieces(self, l, length):
        res = 0
        for i in l:
            res += i // length
        return res