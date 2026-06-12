"""
JS code for finding the length of the longest substring without repeating characters:

what is the input and output of the function?The input of the function is a string `s`,
and the output is an integer representing the length of the longest substring without
repeating characters in the input string `s`.
function lengthOfLongestSubstring(s) {
  let seen = {};
  let left = 0;
  let maxLength = 0;
  for (let right = 0; right < s.length; right++) {
    if (seen[s[right]] !== undefined && seen[s[right]] >= left) {
      left = seen[s[right]] + 1;
    }
    seen[s[right]] = right;
    maxLength = Math.max(maxLength, right - left + 1);
  }
  return maxLength;
}

In python, the hash map is implemented using a dictionary.


"""

def length_of_longest_substring(s):
    seen = {}
    left = 0
    max_length = 0
    for right in range(len(s)):  # using range to iterate through the string
        if s[right] in seen and seen[s[right]] >= left:
            left = seen[s[right]] + 1
        seen[s[right]] = right
        max_length = max(max_length, right - left + 1)
    return max_length


