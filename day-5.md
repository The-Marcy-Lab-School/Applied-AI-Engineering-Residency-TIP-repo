# Day 5

Problem: 3
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
Input: [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]

Algorith:
1. Sort the array in ascending order so the two pointers can make smart directional decisions
2. Create a variable to store your result triplets, starting as an empty array
3. Loop over each number as your "fixed" element (stop 2 early since you need 3 numbers)
4. In the loop, skip the current number if it's the same as the previous one to avoid duplicate triplets
5. If it's not a duplicate, set a left pointer to just after the fixed element and a right pointer to the end of the array
6. While left is less than right, check the sum of all three numbers:
- If the sum equals 0, save the triplet, then skip over any duplicate values on both sides before moving the pointers inward
- If the sum is less than 0, move the left pointer right since you need a bigger number
- If the sum is greater than 0, move the right pointer left since you need a smaller number
7. Return the result array after you finish iterating over all fixed elements


Python Solution:


```py
# solution here
def three_sum(nums):
    result = []
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
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
