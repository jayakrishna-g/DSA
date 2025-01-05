#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def get_rev(self, num):
        rev = 0
        while num > 0:
            rev = rev * 10 + (num % 10)
            num //= 10
        return rev

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True

        original = x
        reversed = self.get_rev(x)

        return original == reversed


# @lc code=end
