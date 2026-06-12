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
a string of letters
Output:
length of substring with the longest non duplicate letters
Algorith:

Python Solution:

```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            if seen.get(s[right]) is not None and seen.get(s[right]) >= left:
                left = seen[s[right]] + 1
            seen[s[right]] = right
            max_length = max(max_length, right - left + 1)
        return max_length
```
