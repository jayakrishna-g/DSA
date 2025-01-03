#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen_set = {}
        for idx, i in enumerate(nums):
            if target - i in seen_set:
                return [seen_set[target - i], idx]

            seen_set[i] = idx


# @lc code=end
