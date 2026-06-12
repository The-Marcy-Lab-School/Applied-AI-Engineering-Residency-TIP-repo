# Day 3

Problem: Reverse String
leetcode link: https://leetcode.com/problems/reverse-string/description/

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
Input: Array of characters

Output: Array of characters

Algorith:
1. Create two pointers:
- left starts at the beginning.
- right starts at the end.
3. Swap the characters at both pointers.
4. Move left forward and right backward.
5. Continue until pointers meet.


Python Solution:

```py
# solution here
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s)-1
        while left <= right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1
```

Problem: Longest Substring Without Repeating Characters
leetcode link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

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
Input: String

Output: integer

Algorith:
1. Use two pointers:
- left tracks the start of the window.
- right expands the window.
2. Store the last index of each character.
3. If a duplicate character appears:
- Move left past the previous occurrence.
4. Calculate the current window size.
5. Track the maximum length.


Python Solution:

```py
# solution here
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        for i in range(len(s)):
            seen = set()
            size = 0
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
                size += 1
            maxLength = max(size, maxLength)
        return maxLength
```
