class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        # for i in range(len(prices)-1):
        #     for j in range(i, len(prices)):
        #         if j > i:
        #             profit= max(profit,prices[j]-prices[i] )
        # return profit
        
        l, r = 0 , 1
        buy=l
        profit =0
        while r < len(prices):
            if prices[r] > prices[l]:
                profit= max(profit,prices[r]-prices[l])
                r += 1
            else:
                l =r
                r += 1
        return profit




            
 
            