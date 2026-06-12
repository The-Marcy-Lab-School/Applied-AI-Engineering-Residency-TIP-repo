# Day 2

Problem: 
leetcode link:

```js
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
Input:

Output:

Algorith:


Python Solution:

```py
def maxProfit(self, prices: List[int]) -> int:
  min_price = float(inf)
  max_profit = 0
  for i in range(len(prices)):
  if prices[i] < min_price:
    min_price = prices[i]
  elif (prices[i] - min_price) > max_profit:
    max_profit = prices[i] - min_price
  return max_profit
```
