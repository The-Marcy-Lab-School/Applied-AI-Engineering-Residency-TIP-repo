# Day 3
function reverseString(s) {

  for (let left = 0, right = s.length - 1; left < right; left++, right--) {
    
    let temp = s[left];
    s[left] = s[right];
    s[right] = temp;
  }
}






def reverseString(s):
    left = 0
    right = len(s) - 1

    for _ in range(len(s) // 2):
  
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
        left += 1
        right -= 1