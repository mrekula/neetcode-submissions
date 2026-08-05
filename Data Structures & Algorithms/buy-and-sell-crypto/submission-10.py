class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]

        for i in range(len(prices)):
            buy = min(buy, prices[i])
            if prices[i] > buy:
                profit = max(prices[i]-buy, profit)
        return profit
