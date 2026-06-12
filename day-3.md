# Day 3

Problem: Reverse String

leetcode link:
https://leetcode.com/problems/reverse-string/submissions/2028747914 [solution]

```js
//js solution
function reverseString(s) {
  let left = 0;
  let right = s.length - 1;
  while (left < right) {
    let temp = s[left];
    s[left] = s[right];
    s[right] = temp;
    left++;
    right--;
  }
  return s;
```
*Input:*\
s = ["h","e","l","l","o"]\
<!-- array of strings-->
*Output:*\
["o","l","l","e","h"]\
<!-- reversed array of strings -->
*Algorithm:*
1. Set two pointers
2. While loop so when the pointers meet/overlap the loop ends
3. Implement a three step swap by reassigning indicies
* Have to have a variable store starting temp value so it isn't lost in memory
4. Increment left and right pointers once the swap is completed.

Python Solution:

```py
lass Solution(object):
    def reverseString(self, s):
        left = 0
        right = len(s) - 1
        while left < right: 
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1
```

