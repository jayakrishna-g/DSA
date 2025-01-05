#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start

# NEED TO REVISIT MISSING LOGIC FOR NEGATIVE TRACKING
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        prod = 1
        INT_MIN = -1 * (2**31)
        INT_MAX = (2**31) - 1

        lim = INT_MAX

        if x < 0:
            prod = -1
            x = -1 * x
            lim = INT_MIN * -1
        while x > 0:
            l = x % 10
            if rev >= lim // 10:
                return 0
            rev *= 10
            if rev >= lim - l:
                return 0
            rev += l

        return rev * prod


# @lc code=end
