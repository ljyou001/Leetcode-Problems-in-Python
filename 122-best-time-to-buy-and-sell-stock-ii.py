class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = prices[0]
        res = 0
        for i in prices:
            if i > prev:
                res = res + i - prev
            prev = i
        return res

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        high = prices[0]
        low = prices[0]
        res = 0
        for i in prices:
            if i > high:
                high = i
            if i < high:
                res = res + high - low
                low = i
                high = i
        res = res + high - low
        return res 