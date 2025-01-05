#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
# LOOK MORE OPTIMAL WAY WITHOUT STACK
class Solution:
    def isValid(self, s: str) -> bool:
        # def helper(opening, closing) -> bool:
        #     c = 0
        #     for i in s:
        #         if i == opening:
        #             c += 1
        #         if i == closing:
        #             if c <= 0:
        #                 return False
        #             c -= 1
        #     return c == 0

        # return helper("(", ")") and helper("[", "]") and helper("{", "}")

        opening = ["(", "{", "["]
        closing = [")", "}", "]"]
        stack = []

        for i in s:
            if i in opening:
                stack.append(i)

            if i in closing:
                if len(stack) == 0:
                    return False
                close_idx = closing.index(i)
                open_idx = opening.index(stack[-1])

                if open_idx != close_idx:
                    return False

                stack.pop()

        return len(stack) == 0


# @lc code=end
