# Day 1

Problem: FizzBuzz

leetcode link: [https://leetcode.com/problems/fizz-buzz/](https://leetcode.com/problems/fizz-buzz/)

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

Input: `n = 15`

Output: `["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]`

Algorith:

Python Solution:

```py
def fizzBuzz(n):
    result = []

    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))

    return result
```
