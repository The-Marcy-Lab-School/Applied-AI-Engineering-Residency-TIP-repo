# Day 5

Problem:
leetcode link: https://leetcode.com/problems/palindrome-number/description/

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

Input: `121`

Output: `true`

Algorithm: two pointers

Python Solution:

```py
# solution here
def isPalindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    n = x
    reverse = 0
    while x > reverse:
        reverse = reverse * 10 + n % 10
        n = n // 10
    if reverse == x:
            return True
    return False
```

Problem:
leetcode link:

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

Input: `nums = [-1,0,1,2,-1,-4]`

Output: `[[-1,-1,2],[-1,0,1]]`

Algorithm:

Python Solution:

```py
# solution here
def threeSum(self, nums: list[int]) -> list[list[int]]:
     output = []
     nums.sort()
     for i, num in enumerate(nums):
         if i > 0 and nums[i - 1] == num:
             continue
         l = i + 1
         r = len(nums) - 1
         while l < r:
             sum = num + nums[l] + nums[r]

             if sum == 0:
                 output.append([num, nums[l], nums[r]])
                 l += 1
                 while nums[l] == nums[l - 1] and l < len(nums) - 1:
                     l += 1
             elif sum > 0:
                 r -= 1

             else:
                 l += 1
     return output
```
