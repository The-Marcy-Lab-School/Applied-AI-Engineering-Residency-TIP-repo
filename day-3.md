# Day 3

## JavaScript code 

### Reverse String -- JavaScript Solution
```js
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
### Longest Substring Without Repeating Characters -- JavaScript Solution
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



## Python code 

### Reverse String -- Python Solution
```python
def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
```
### Longest Substring Without Repeating Characters -- Python Solution
```python
def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        max_length = 0
        for right, char in enumerate(s):
            if char in seen and seen[char] >= left:
                left = seen[s[right]] + 1
    
            seen[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length
```