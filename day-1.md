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
Input: an integer n

Output: an array of strings

Algorith:

1. Create an empty result array.
2. Loop from 1 to n inclusive.
3. For each number:
  - Check if divisible by both 3 and 5.
  - Else check if divisible by 3.
  - Else check if divisible by 5.
  - Otherwise add the number as a string.
4. Return the result array.

Python Solution:

```py
# solution here
    def fizzBuzz(self, n: int) -> List[str]:
        list = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                list.append("FizzBuzz")
            elif i % 3 == 0:
                list.append("Fizz")
            elif i % 5 == 0:
                list.append("Buzz")
            else:
                list.append(str(i))
        return list        
        
```
