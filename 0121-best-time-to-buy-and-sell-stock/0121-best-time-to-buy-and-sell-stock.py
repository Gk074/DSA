class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = float('inf')
        if len(prices) == 1:
            return 0
        for p in prices:
            min_price = min(min_price,p)
            max_profit = max(max_profit, p - min_price)
        return max_profit 