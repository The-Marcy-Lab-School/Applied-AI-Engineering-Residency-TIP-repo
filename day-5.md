# Day 5

Problem: Palindrome Number
leetcode link: https://leetcode.com/problems/palindrome-number/

```js
//js solution
function isPalindrome(x) {
  if (x < 0) return false;
  const str = x.toString();
  let left = 0;
  let right = str.length - 1;
  while (left < right) {
    if (str[left] !== str[right]) return false;
    left++;
    right--;
  }
  return true;
}
```
*Input:*\
x: an integer\
*Output:*\
True/False based on whether the number is a palindrome or not\
*Algorithm:*
1. Set a conditional for negative numbers
2. Turn x into a string the compare each individual number in the integer and set two pointer variables
3. Set a while loop that stops once the pointers meet/overlap
4. Set a conditional to check if the integer is a palindrome

Python Solution: https://leetcode.com/problems/palindrome-number/submissions/2030984763

```py
# solution here
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        s = str(x)
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
```
