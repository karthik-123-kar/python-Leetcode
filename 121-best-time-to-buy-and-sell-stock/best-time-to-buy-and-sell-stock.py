class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        mini_price = prices[0]
        max_price = 0
        for i in range(1,n):
            if prices[i] < mini_price: 
                mini_price = prices[i]
            else:
                profit = prices[i] - mini_price
                if profit > max_price:
                    max_price = profit
        return max_price
