# Day 5

Problem:3Sum
leetcode link:https://leetcode.com/problems/3sum/

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

Input: Array of numbers

Output: Array of Arrays

Algorith: Sort the array from smallest to largest this is what makes the two pointer approach possible.
Loop through each number with an i pointer, using it as the fixed first number of the triplet.

If the current number is the same as the previous one, skip it to avoid duplicate triplets.
