# Day 5

Problem: 
leetcode link:

```js
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
Input:

Output:

Algorith:


Python Solution:

```py
def threeSum(self, nums: list[int]) -> list[list[int]]:
  res = []
  nums.sort()
  for i in range(len(nums)-2):
    if (i > 0) and (nums[i] == nums[i-1]):
      continue
    l = i + 1
    r = len(nums) - 1
    while l < r:
      total = (nums[i] + nums[l] + nums[r])
      if total == 0:
        res.append([nums[i], nums[l], nums[r]])
        while l < r and nums[l] == nums[l+1]:
          l += 1
        while l < r and nums[l] == nums[l+1]:
          r -= 1
        l += 1
        r -= 1
      elif total < 0:
        l += 1
      else:
        r -= 1
  return res
```
