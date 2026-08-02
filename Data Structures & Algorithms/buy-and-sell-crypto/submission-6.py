class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit=0
        # for i in range(len(prices)-1):
        #     for j in range(i, len(prices)):
        #         if j > i:
        #             profit= max(profit,prices[j]-prices[i] )
        # return profit

        left, right, profit= 0, 1,0

        while right < len(prices):
            if prices[right] > prices[left]:
                profit= max(profit,prices[right]-prices[left] )
            else:
                left= right
            right += 1
        return profit
        
       



            
 
            