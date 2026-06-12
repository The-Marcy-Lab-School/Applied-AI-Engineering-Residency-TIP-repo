# Day 3

Problem: Longest Substring Without Repeating Characters
leetcode link:https://leetcode.com/problems/longest-substring-without-repeating-characters/

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

Input:String

Output:number

Algorith: Declare an empty seen dictionary, left pointer with a value of 0, and maxLength with a value of 0.

Move a right pointer through every character in the string one by one.
For each character, ask: have we seen this character before, and is it inside our current window?

Yes — move the left pointer to one position after where we last saw it, shrinking the window to remove the duplicate.
No — leave the window as is.

Record the current character's position in seen.
Calculate the current window size (right - left + 1) and update maxLength if it's the biggest we've seen.
After going through all characters, return maxLength.

Python Solution:

```py
# solution here
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        max_length = 0
        for right in range(len(s)):
            if s[right] in seen and seen [s[right]] >= left:
                left = seen[s[right]] + 1
            seen[s[right]] = right
            max_length = max(max_length, right - left + 1)
        return max_length
```
