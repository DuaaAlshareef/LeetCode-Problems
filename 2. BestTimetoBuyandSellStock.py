from typing import List
'''Looping through the array, keep updating the minimum number, find the max difference between the
next elements in the array and that number.
Time Complexity: O(n), loop through the array one time.
Space Complexity: O(1), only storing variables. '''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_price = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            minimum_price = min(minimum_price, prices[i])
            current_profit = prices[i] - minimum_price
            max_profit = max(current_profit, max_profit)
        return max_profit
    







