#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = []
        gap = numRows - 1
        ri = 0
        si = 0
        while si < len(s):
            row = [""] * numRows
            if ri % gap == 0:
                c = numRows
                while si < len(s) and c > 0:
                    row[numRows - c] = s[si]
                    si += 1
                    c -= 1
            else:
                idx = numRows - (ri % gap) - 1
                row[idx] = s[si]
                si += 1
            ri += 1

            res.append(row)
        # print(res)
        ans = ""
        for j in range(numRows):
            for i in range(0, len(res)):
                ans += res[i][j]
        return ans


# @lc code=end
