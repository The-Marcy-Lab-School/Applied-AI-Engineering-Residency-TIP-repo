# Day 2

Problem: Two Sum

leetcode link: https://leetcode.com/problems/two-sum/

```js
//js solution
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
*Input:*\
nums: array of integers\
target: integer\
*Output:*\
Indicies of the two nums that sum to target\
*Algorithm:*
1. Loop through nums twice to set two pointers
2. If statement to check if the values of both pointers === target

Python Solution:https://leetcode.com/problems/two-sum/submissions/2029846516

```py
# solution here
class Solution(object):
    def twoSum(self, nums, target):
        for i in range (len(nums)):
            for j in range (i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]
```
