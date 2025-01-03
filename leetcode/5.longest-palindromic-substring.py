#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = [0, 0]

        def expand(st, en, ans):
            if st < 0 or st >= len(s) or en < 0 or en >= len(s) or s[st] != s[en]:
                return
            while st >= 0 and en < len(s):
                if s[st] != s[en]:
                    break
                st -= 1
                en += 1

            st += 1
            en -= 1

            if (ans[1] - ans[0]) < (en - st):
                ans[0], ans[1] = st, en

        for i in range(1, len(s)):
            expand(i - 1, i + 1, ans)
            expand(i - 1, i, ans)

        print(ans)

        return s[ans[0] : ans[1] + 1]


# @lc code=end
