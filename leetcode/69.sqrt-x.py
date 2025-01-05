#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 0
        hi = x
        while lo <= hi:
            mid = (lo + hi) // 2
            prev = mid - 1
            prev2, mid2 = prev * prev, mid * mid

            if mid2 == x:
                return mid

            if prev2 <= x < mid2:
                return prev

            if x <= mid2:
                hi = mid - 1

            else:
                lo = mid + 1

        return lo if lo * lo == x else hi


# @lc code=end
