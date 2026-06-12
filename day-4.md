# Day 4

Problem:
leetcode link: https://leetcode.com/problems/contains-duplicate/description/

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

Input: `[1,2,3,1]`

Output: `true`

Algorithm:

Python Solution:

```py
# solution here
def containsDuplicate(self, nums: List[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

Problem:
leetcode link: https://leetcode.com/problems/group-anagrams/description/

```js
//js solution
function groupAnagrams(strs) {
  const map = {};
  for (let i = 0; i < strs.length; i++) {
    const key = strs[i].split("").sort().join("");
    if (map[key] === undefined) {
      map[key] = [];
    }
    map[key].push(strs[i]);
  }
  return Object.values(map);
}
```

Input: ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Algorithm:

Python Solution:

```py
# solution here
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    map = {}
    for string in strs:
        key = ''.join(sorted(string))
        if key not in map:
            map[key] = []
        map[key].append(string)
    return [value for value in map.values()]
```
