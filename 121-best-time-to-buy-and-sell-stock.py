class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        res = 0
        profit = 0
        while j < len(prices):
            profit = prices[j] - prices[i]
            res = max(res, profit)
            if prices[j] < prices[i]:
                i = j
            j += 1
        return res