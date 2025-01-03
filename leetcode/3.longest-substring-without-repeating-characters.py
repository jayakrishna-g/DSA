#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start

from collections import deque


class Helper:
    def __init__(self):
        self.seen_till_now = deque()
        self.bit_mask = 0

    def get_mask(self, char):
        return 1 << ord(char)

    def add(self, ele):
        if ele in self.seen_till_now:
            # raise ValueError(f"{ele} is already in seen_till_now")
            return
        self.bit_mask |= self.get_mask(ele)
        self.seen_till_now.append(ele)

    def check(self, ele):
        return self.bit_mask & self.get_mask(ele)

    def remove(self, ele):
        while self.seen_till_now[0] != ele:
            self.bit_mask ^= self.get_mask(self.seen_till_now[0])
            self.seen_till_now.popleft()
        self.bit_mask ^= self.get_mask(self.seen_till_now[0])
        self.seen_till_now.popleft()

    @property
    def length(self):
        return len(self.seen_till_now)


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen_ele = Helper()
        ans = 0
        for char in s:
            if seen_ele.check(char):
                ans = max(ans, seen_ele.length)
                seen_ele.remove(char)
            seen_ele.add(char)

        ans = max(ans, seen_ele.length)

        return ans


# @lc code=end
