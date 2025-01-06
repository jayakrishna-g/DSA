#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
from collections import Counter


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = Counter(nums)
        return any(count > 1 for count in hash.values())


# @lc code=end
