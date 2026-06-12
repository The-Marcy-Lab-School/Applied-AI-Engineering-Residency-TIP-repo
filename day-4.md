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
Input: Array of integers

Output: boolean

Algorith:
1. Create an empty set.
2. Loop through the array.
3. For each number:
- If it already exists in the set duplicate found.
- Otherwise add it to the set.
4. If the loop finishes, no duplicates exist.


Python Solution:

```py
# solution here
def containsDuplicate(self, nums):
  seen = set()
  for num in nums:
    if num in seen:
      return True
    seen.add(num)
  return False
```


Problem: Group Anagrams
leetcode link: https://leetcode.com/problems/group-anagrams/

```js
//js solution
function groupAnagrams(strs) {
  const map = {};
  for (let i = 0; i < strs.length; i++) {
    const key = strs[i].split('').sort().join('');
    if (map[key] === undefined) {
      map[key] = [];
    }
    map[key].push(strs[i]);
  }
  return Object.values(map);
}
```
Input: Array of strings

Output: Array of Array of strings

Algorith:
1. Create a hash map.
2. For each word:
- Sort the letters.
- Use the sorted string as a key.
3. Add the original word to the matching group.
4. Return all groups.


Python Solution:

```py
# solution here
def groupAnagrams(self, strs):
  groups = {}
  for word in strs:
    key = ''.join(sorted(word))
    if key not in groups:
      groups[key] = []
    groups[key].append(word)
  return list(groups.values())
```
