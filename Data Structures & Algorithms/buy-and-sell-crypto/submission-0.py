class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0

        for i,num in enumerate(prices):
            if i < len(prices)-1:
                print(i)
                temp=max(prices[i+1:])-num
                profit=max(profit, temp)
        return profit
        