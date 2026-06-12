# Day 2

Problem: Best Time To Buy And Sell Stock
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
Input: [7,1,5,3,6,4]

Output: 5

Algorith:
1. Create a variable for the minimun price and set it to infinite 
2. Create a variable for the max profit starting at 0
3. loop over the prices to find get your minimun price and max profit
4. In the loop check if the price for the day is less than the minimun price and change the minimun price for that day if true
5. If the minimun price isn't being updated then check if the price for the day - the money already spent from the minimun day price is greater than the max profit. If true then update the max profit to your minimun price for that day.
6. Return the max profit after we stop iterating over the prices.

Python Solution:

```py
# solution here

def max_profit(prices):
    minPrice = float('inf')
    maxProfit = 0

    for i in prices:
        if i < minPrice:
            minPrice = i
        elif i - minPrice > maxProfit:
            maxProfit = i - minPrice
    
    return maxProfit
    
print(max_profit([7,1,5,3,6,4]))
```
