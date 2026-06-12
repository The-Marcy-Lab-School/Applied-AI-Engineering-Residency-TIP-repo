# Day 2

Problem: Two Sum
leetcode link: https://leetcode.com/problems/two-sum/description/

```js
//js solution
function twoSum(nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }
}
```
Input: Array of integers `nums` and integer `target`

Output: an array of two indicies that add up to `target`

Algorith:
1. Loop through every number.
2. Compare it with every number after it.
3. If the two numbers add up to the target Return their indices.


Python Solution:

```py
# solution here
def twoSum(self, nums, target):
  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      if nums[i] + nums[j] == target:
        return [i, j]
```

Problem: Best Time To Buy and Sell Stock
leetcode link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

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
Input: array of stock prices

Output: maximum profit

Algorith: 
1. Keep track of the lowest price seen so far.
2. For each price:
- Update minimum price if current price is lower.
- Otherwise calculate possible profit.
3. Keep the maximum profit found.
4. Return maximum profit.


Python Solution:

```py
# solution here
def maxProfit(self, prices):
  minPrice = float("inf")
  maxProfit = 0
  for price in prices:
    if price < minPrice:
      minPrice = price
    elif price - minPrice > maxProfit:
      maxProfit = price - minPrice
  return maxProfit
```
