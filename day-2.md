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
array
Output:
number of the profit
Algorith:

Python Solution:

```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = math.inf
        max_profit = 0

        for num in range(len(prices)):
            if prices[num] < min_price:
                min_price = prices[num]
            elif prices[num] - min_price >      max_profit:
                max_profit = prices[num] - min_price
        return max_profit
```
