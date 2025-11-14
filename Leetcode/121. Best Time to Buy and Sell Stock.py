from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
         min_price = float('inf')
         max_profit = 0

         for price in prices:
            ass = price - min_price
            if price < min_price:
                min_price = price
            elif ass> max_profit:
                max_profit = ass

         return max_profit