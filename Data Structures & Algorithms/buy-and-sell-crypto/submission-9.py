class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # minb = prices[0]
        # profit = 0

        # for sell in prices:
        #     profit = max(profit, sell - minb)
        #     minb = min(minb, sell)
        # return profit
        

        b, s = 0 , 1
        profit = 0

        while s < len(prices):
            if prices[s] < prices[b]:
                b = s
            else:
                profit = max(profit, prices[s]-prices[b])
            s += 1
        return profit
