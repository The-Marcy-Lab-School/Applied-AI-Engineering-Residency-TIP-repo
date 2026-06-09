# Day 2

Problem:
leetcode link: https://leetcode.com/problems/two-sum/

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

Input: `nums = [2,7,11,15], target = 9`

Output: `[0, 1]`

Algorithm: Nested for loops // Brute force

Python Solution:

```py
# solution here
def twoSum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```

Problem:
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

Input: `prices = [7,1,5,3,6,4]`

Output: `5`

Algorithm: Two pointers

Python Solution:

```py
# solution here
def maxProfit(prices):
    minimum = float('inf')
    maxSell = 0

    for num in prices:
        if num < minimum:
            minimum = num
            continue
        if num - minimum > maxSell:
            maxSell = num - minimum

    return maxSell
```
