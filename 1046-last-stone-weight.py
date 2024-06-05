from heapq import heappush, heappop, heapify

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [i * -1 for i in stones]
        heapify(stones)

        while len(stones) > 1:
            stone1 = heappop(stones)
            stone2 = heappop(stones)
            # new_stone = abs(stone1 - stone2)
            # if new_stone > 0:
            if stone1 != stone2:
                heappush(stones, stone1 - stone2)

        return stones[0] * -1 if stones else 0