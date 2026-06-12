# Day 3

Problem:

leetcode link:

```js
//js solution
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

Input: `s = "abcabcbb"`

Output: `3`

Algorith:

Python Solution:

```py
def lengthOfLongestSubstring(s):
    seen = {}
    left = 0
    maxLength = 0

    for right in range(len(s)):
        if s[right] in seen and seen[s[right]] >= left:
            left = seen[s[right]] + 1

        seen[s[right]] = right
        maxLength = max(maxLength, right - left + 1)

    return maxLength
```
