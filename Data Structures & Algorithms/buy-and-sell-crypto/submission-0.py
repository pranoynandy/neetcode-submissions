class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        res = 0
        for sell in range(1,len(prices)):
            profit = prices[sell] - prices[buy]
            if  profit >= 0:
                res = max(res, profit)
            else:
                buy = sell

        return res
            



        