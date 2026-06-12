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
Input: integer `x`

Output: boolean

Algorith:
1. If x is negative return false.
2. Convert number to string.
3. Use two pointers:
- left at start
- right at end
4. Compare characters.
5. If mismatch return false.
6. If all match return true.


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

Problem: Three Sum
leetcode link: https://leetcode.com/problems/3sum/

```js
//js solution
function threeSum(nums) {
  const result = [];
  nums.sort((a, b) => a - b);
  for (let i = 0; i < nums.length - 2; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    let left = i + 1;
    let right = nums.length - 1;
    while (left < right) {
      const sum = nums[i] + nums[left] + nums[right];
      if (sum === 0) {
        result.push([nums[i], nums[left], nums[right]]);
        while (left < right && nums[left] === nums[left + 1]) left++;
        while (left < right && nums[right] === nums[right - 1]) right--;
        left++;
        right--;
      } else if (sum < 0) {
        left++;
      } else {
        right--;
      }
    }
  }
  return result;
}
```
Input: Array of integers

Output: Array of tuples

Algorith:
1. Sort the array.
2. Fix one number (i).
3. Use two pointers:
- left = i + 1
- right = end
4. Move pointers based on sum:
- sum == 0 → record result
- sum < 0 → move left
- sum > 0 → move right
5. Skip duplicates to avoid repeated triplets.


Python Solution:

```py
# solution here
def threeSum(self, nums):
  nums.sort()
  result = []
  for i in range(len(nums) - 2):
    if i > 0 and nums[i] == nums[i - 1]:
      continue
    left, right = i + 1, len(nums) - 1
    while left < right:
      total = nums[i] + nums[left] + nums[right]
      if total == 0:
        result.append([nums[i], nums[left], nums[right]])
        while left < right and nums[left] == nums[left + 1]:
        left += 1
        while left < right and nums[right] == nums[right - 1]:
        right -= 1
      left += 1
      right -= 1
    elif total < 0:
      left += 1
    else:
      right -= 1
  return result
```
