class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = prices[0]

        for sell in prices:
            profit = sell-minBuy
            maxProfit = max(maxProfit, profit)
            minBuy = min(sell, minBuy)
    
        return maxProfit