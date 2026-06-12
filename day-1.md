# Day 1

Problem: FizzBuzz

leetcode link: https://leetcode.com/problems/fizz-buzz/

```js
function fizzBuzz(n) {
  const result = [];
  for (let i = 1; i <= n; i++) {
    if (i % 15 === 0) {
      result.push('FizzBuzz');
    } else if (i % 3 === 0) {
      result.push('Fizz');
    } else if (i % 5 === 0) {
      result.push('Buzz');
    } else {
      result.push(String(i));
    }
  }
  return result;
}
```
Input: 3

Output: ["1","2","Fizz"]

Algorith:
1. Create a variable which represents the output array
2. Loop starting from 1 to the input
3. In the loop, check if the current number is divisible by 15 first and push 'FizzBuzz' if true
- If not, check if it's divisible by 3 and push 'Fizz' if true
- If not, check if it's divisible by 5 and push 'Buzz' if true
- If none of those conditions are met, push the number into the array
4. Return the result list after you finish iterating

Python Solution:

```py
# solution here
def fizz_buzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append('FizzBuzz')
        elif i % 3 == 0:
            result.append('Fizz')
        elif i % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(i))
    return result
```
