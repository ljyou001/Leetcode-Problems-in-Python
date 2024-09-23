import heapq

class Solution:
    """
    @param boxes: number of pens for each box
    @param target: the target number
    @return: the minimum boxes
    """
    def minimum_boxes(self, boxes: List[int], target: int) -> int:
        # write your code here
        if not boxes:
            return -1
        
        left = 0
        right = 0
        total = 0
        length = []
        while right < len(boxes):
            total += boxes[right]
            while left < right and total > target:
                total -= boxes[left]
                left += 1
            if total == target:
                heapq.heappush(length, (right - left + 1))
                left = right + 1
                total = 0
            right += 1
        
        if len(length) < 2:
            return -1
        
        minlen = heapq.heappop(length) + heapq.heappop(length)
        return minlen