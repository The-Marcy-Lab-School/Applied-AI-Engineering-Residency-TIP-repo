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
  https://docs.google.com/presentation/d/1t1DjKp6bAFDN05BHgYkRhw7ax-FlmWBhtIXCI_K9grs/edit?slide=id.p6#slide=id.p6
}
```
*Input:*\
n: integer\
*Output:*\
A string either 'Fizz', 'FizzBuzz', 'Buzz', or integer as a string\
*Algorithm:*
1. Set a result array
2. Set a conditional


Python Solution:https://leetcode.com/problems/fizz-buzz/submissions/2028769564

```py
class Solution(object):
  def fizzBuzz(self, n):
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
