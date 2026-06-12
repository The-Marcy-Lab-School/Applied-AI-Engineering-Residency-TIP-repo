# Day 5

## JavaScript code 

### Palindrome Number -- JavaScript Solution
```js
function isPalindrome(x) {
  if (x < 0) return false;
  const str = x.toString();
  let left = 0;
  let right = str.length - 1;
  while (left < right) {
    if (str[left] !== str[right]) return false;
    left++;
    right--;
  }
  return true;
}
```
### Three Sum -- JavaScript Solution

```js
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



## Python code 

### Palindrome Number -- Python Solution
```python
def isPalindrome(self, x: int) -> bool:
        string = str(x)
        left = 0
        right = len(string) - 1

        while (left < right):
          if string[left] != string[right]:
            return False
          left += 1
          right -= 1

        return True  
```
### Three Sum -- JavaScript Solution
```python
def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()  

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
        
            left = i + 1
            right = len(nums) - 1
    
            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]
        
                if total_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
            
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                
                    left += 1
                    right -= 1
                elif total_sum < 0:
                    left += 1
                else:
                    right -= 1

        return result
```