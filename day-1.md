# Day 1

Problem: FizzBuzz

leetcode link: https://leetcode.com/problems/fizz-buzz/

```js
function fizzBuzz(n) {
  const result = [];
  for (let i = 1; i <= n; i++) {
    if (i % 15 === 0) {
      result.push("FizzBuzz");
    } else if (i % 3 === 0) {
      result.push("Fizz");
    } else if (i % 5 === 0) {
      result.push("Buzz");
    } else {
      result.push(String(i));
    }
  }
  return result;
}
```

Input:
A number
Output:
An array
Algorith:
if n is divisible by 3, 5 or 3 and 5 then return 'Fizz', 'Buzz' or 'FizzBuzz' else return n in a string
Python Solution:

```py
class Solution(object):
    def fizzBuzz(self, n):
        results = []
        for num in range(1, n + 1):
            if num % 15 == 0:
                results.append('FizzBuzz')
            elif num % 3 == 0:
                results.append('Fizz')
            elif num % 5 == 0:
                results.append('Buzz')
            else:
                results.append(str(num))
        return results
```
