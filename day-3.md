# Day 3

Problem:
leetcode link: https://leetcode.com/problems/reverse-string/

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
}
```

Input: ["h","e","l","l","o"]

Output: ["o","l","l","e","h"]

Algorithm: Two pointers

Python Solution:

```py
# solution here
def reverseString(s):
    l = 0
    r = len(s) - 1

    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

    return s
```

Problem:
leetcode link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

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

Input: `"abcabcbb"`

Output: 3

Algorithm: Frequency counter

Python Solution:

```py
# solution here
def lengthOfLongestSubstring(self, s: str) -> int:
    seen = {}
    l = 0
    maxLength = 0
    for r in range(len(s)):
        if seen.get(s[r], None) != None and seen.get(s[r]) >= l:
            l = seen[s[r]] + 1
        seen[s[r]] = r
        maxLength = max(maxLength, r - l + 1)
    return maxLength
```
