# Day 4


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








 def contains_duplicate(nums):
    seen = set()

    for i in range(len(nums)):
        if nums[i] in seen:
            return True

        seen.add(nums[i])

    return False