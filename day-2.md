# Day 2


Problem 2: Two-Sum

leetcode link: https://leetcode.com/problems/two-sum/description/ 

```js
function twoSum(nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }
}
```
Input: List[int]

Output:

Algorithm:


Python Solution:

```py
# solution here
# a list can only contain the same value types in a list in python.
def (self, nums: List[int], target: int) -> List[int] 
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

```
