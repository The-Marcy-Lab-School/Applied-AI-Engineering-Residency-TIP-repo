# Day 3

Problem: 
leetcode link:

```js
function lengthOfLongestSubstring(s) {
  let seen = {};
  let left = 0;
  let maxLength = 0;
  for (let right = 0; right < s.length; right++) {
    if (seen[s[right]] !== undefined && seen[s[right]] >= left) {
      left = seen[s[right]] + 1;
    }
    seen[s[right]] = right;
    maxLength = Math.max(maxLength, right - left + 1);
  }
  return maxLength;
}
```
Input:

Output:

Algorith:


Python Solution:

```py
def lengthOfLongestSubstring(self, s: str) -> int:
    seen = {}
    left = 0
    maximum = 0
    for right in range(len(s)-1):
        if (s[right] in seen) and seen[s[right]] >= left:
            left = seen[s[right]] + 1
        seen[s[right]] = right
        maximum = max(maximum, right - left + 1)
    return maximum
```
