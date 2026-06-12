# Day 5


Problem 5: Palindrome Number

Leetcode Link:


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



Input:

Output:

Algorithm:


Python Solution:

```py
# solution here
 def isPalindrome(self, x: int) -> bool:
    if x < 0:
            return False
    s = str(x)
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
                return False
        left += 1
        right -= 1
    return True

```