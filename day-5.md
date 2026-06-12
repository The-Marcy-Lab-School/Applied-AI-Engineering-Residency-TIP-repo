# Day 5
def isPalindrome(x):
    if x < 0:
        return False

    s = str(x)
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True