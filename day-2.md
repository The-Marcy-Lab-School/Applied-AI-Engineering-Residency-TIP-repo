# Day 2

Problem: Best Time to Buy and Sell Stock
leetcode link:https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

```js
//js solution
function maxProfit(prices) {
  let minPrice = Infinity;
  let maxProfit = 0;
  for (let i = 0; i < prices.length; i++) {
    if (prices[i] < minPrice) {
      minPrice = prices[i];
    } else if (prices[i] - minPrice > maxProfit) {
      maxProfit = prices[i] - minPrice;
    }
  }
  return maxProfit;
}
```

Input: Array of numbers

Output: Number

Algorith: declare a variable named minPrice with the value of Infinity and a maxProfit with the value of 0.

Then we loop through every price one by one.

For each price we ask is this price lower than the lowest we've seen? if yes update minPrice and now this is the best day to buy, if not would selling today be our best profit so far? we calculate today's profit by subtracting minPrice from the current price. If it's higher than maxProfit, update maxProfit.

In the end after going through all the prices, return maxProfit.

Python Solution:

```py
# solution here
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
```
