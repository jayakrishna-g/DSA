#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for s in strs:
            hash["".join(sorted(s))].append(s)

        return [value for value in hash.values()]


# @lc code=end
