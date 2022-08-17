'''
You are given an array prices where prices[i] is the price of 
a given stock on the ith day.

You want to maximize your profit by choosing a single day to 
buy one stock and choosing a different day in the future to sell 
that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4,9,1]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 
(price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed 
because you must buy before you sell.
'''

def max_profit(nums):

    min_val_seen = nums[0]
    max_profit_seen = 0

    for price in nums:
        min_val_seen = min(price, min_val_seen)
        new_profit = price-min_val_seen
        max_profit_seen = max(max_profit_seen,new_profit)
    
    return max_profit_seen

prices = [7,1,5,3,6,4]
print(max_profit(prices))