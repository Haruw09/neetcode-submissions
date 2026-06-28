class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        max_profit = 0
        for price in prices[1:]:
            max_profit = max(price - min_buy, max_profit)
            min_buy = min(price, min_buy)
        return max_profit