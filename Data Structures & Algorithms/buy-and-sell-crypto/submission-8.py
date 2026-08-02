class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minb = prices[0]
        profit = 0

        for sell in prices:
            profit = max(profit, sell - minb)
            minb = min(minb, sell)
        return profit
        