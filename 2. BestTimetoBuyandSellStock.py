from typing import List
import time

'''
Submitted solution in leetcode:
Looping through the array, keep updating the minimum number, find the max difference between the
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
    
'''
We can do another implementation by explicitly doing the comparisons of the min/max,
while it has the same time and space complexity it performs slightly faster.
Timing both solutions and comparing between the results.
'''
# Sample data
# prices = [7, 1, 5, 3, 6, 4] * 10000  # Making the list large to see the performance difference

# start = time.time()
# def maxProfit_min_max(prices):
#     minimum_price = prices[0]
#     max_profit = 0
#     for i in range(len(prices)):
#         minimum_price = min(minimum_price, prices[i])
#         current_profit = prices[i] - minimum_price
#         max_profit = max(current_profit, max_profit)
#     return max_profit

# print("Max Profit (min/max):", maxProfit_min_max(prices))
# end = time.time()
# print("Time (min/max):", end - start)



'''
Solution using two pointers
'''

# start = time.time()
# def maxProfit_explicit(prices):
#     n=len(prices)
#     l,r = 0,1
#     max_profit = 0
#     mimimum_price = prices[l]
#     while r < n:
#         if prices[l] < mimimum_price:
#             mimimum_price = prices[l]
#         profit = prices[r] - mimimum_price 
#         if profit > max_profit:
#             max_profit=profit
#         r +=1
#         l +=1
#     return max_profit

# print("Max Profit (explicit):", maxProfit_explicit(prices))
# end = time.time()
# print("Time (explicit):", end - start)


# Output:
# Max Profit (min/max): 6
# Time (min/max): 0.011727094650268555
# Max Profit (explicit): 6
# Time (explicit): 0.0035331249237060547
'''Notice the difference in time, we can conclude that when dealing with large arrays
the explicit implementation is faster, due to the function calls in the min/max implementation'''




    




