# Day 4

Problem: Contains Duplicate

leetcode link: https://leetcode.com/problems/contains-duplicate/

```js
//js solution
function containsDuplicate(nums) {
  const seen = new Set();
  for (let i = 0; i < nums.length; i++) {
    if (seen.has(nums[i])) {
      return true;
    }
    seen.add(nums[i]);
  }
  return false;
}
```
*Input:*\
nums: integer array\
*Output:*\
True/false BASED ON if there is a duplicate in the given array
*Algorithm:*\
1. Use Set to identify a duplicate
2. Loop through the nums array
3. Add each num[i] to Set and if there is a duplicate, return false

Python Solution:
https://leetcode.com/problems/contains-duplicate/submissions/2029836363 
```py
# solution here
class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for i in range(len(nums)):
            if(nums[i] in seen):
                return True
            else:
                seen.add(nums[i])
        return False
```
