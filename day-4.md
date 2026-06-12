# Day 4

## JavaScript code 

### Contains Duplicate -- JavaScript Solution
```js
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
### Group Anagrams -- JavaScript Solution

```js
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



## Python code 

### Contains Duplicate -- Python Solution
```python
def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set([])

        for num in nums:
            if num in seen:
                return True
            
            seen.add(num)

        return False
```
### Group Anagrams -- Python Solution
```python
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for string in strs:
            key = ''.join(sorted(string))

            if key not in map:
                map[key] = []

            map[key].append(string)
        
        return list(map.values())
```