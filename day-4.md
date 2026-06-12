# Day 4

Problem:
leetcode link:

```js
javascript;
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

Input:
an array of strings with
Output:
an array of arrays with strings that are anagrams
Algorith:

Python Solution:

```py
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
            key = " ".join(sorted(word))
            if map.get(key) is None:
                map[key] = []
            map[key].append(word)

        return list(map.values())
```
