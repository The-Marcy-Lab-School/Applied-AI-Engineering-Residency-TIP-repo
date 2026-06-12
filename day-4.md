# Day 4

Problem:

leetcode link:

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

def groupAnagrams(strs):
    map = {}

    for i in range(len(strs)):
        key = "".join(sorted(strs[i]))

        if key not in map:
            map[key] = []

        map[key].append(strs[i])

    return list(map.values())
```

Input: `strs = ["eat","tea","tan","ate","nat","bat"]`

Output: `[["eat","tea","ate"],["tan","nat"],["bat"]]`

Algorith:

Python Solution:

```py
def groupAnagrams(strs):
    map = {}

    for i in range(len(strs)):
        key = "".join(sorted(strs[i]))

        if key not in map:
            map[key] = []

        map[key].append(strs[i])

    return list(map.values())
```
