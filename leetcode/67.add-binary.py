#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        a = a[::-1]
        b = b[::-1]
        if len(a) < len(b):
            a, b = b, a

        for idx, i in enumerate(b):
            sum = ord(a[idx]) + ord(b[idx]) - 2 * ord("0") + carry
            res += chr((sum % 2) + ord("0"))
            carry = 1 if sum > 1 else 0

        for idx in range(len(b), len(a)):
            sum = ord(a[idx]) - ord("0") + carry
            res += chr((sum % 2) + ord("0"))
            carry = 1 if sum > 1 else 0

        if carry != 0:
            res += "1"

        return res[::-1]


# @lc code=end
