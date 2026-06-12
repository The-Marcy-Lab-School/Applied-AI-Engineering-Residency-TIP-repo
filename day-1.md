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
Input:
```md
list of numbers
```
Output:
```md
list of nums and strings
```
Algorith:


Python Solution:

```py
def fizzBuzz(self, n: int) -> List[str]:
  answer = []

  for i in range(1, n+1):
    if (i % 3 == 0) and (i % 5 == 0):
      answer.append('FizzBuzz')
    elif i % 5 == 0:
      answer.append('Buzz')
    elif i % 3 == 0:
      answer.append('Fizz')
    else:
      answer.append(str(i))
    i+=1
      
  return(answer)          
```
