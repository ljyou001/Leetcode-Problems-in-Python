class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left + 1 < right:
            mid = (left + right) // 2
            eating_hours = self.eat_hours(piles, mid)
            if eating_hours > h:
                left = mid
            else:
                right = mid
        if self.eat_hours(piles, left) <= h:
            return left
        return right
        
    def eat_hours(self, piles, speed):
        import math
        res = 0
        for i in piles:
            res += (math.ceil(i / speed))
        return res