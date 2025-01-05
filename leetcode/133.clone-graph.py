#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"], vis={}) -> Optional["Node"]:
        if node is None:
            return None
        if node in vis:
            return vis[node]
        new_node = Node(node.val)
        vis[node] = new_node
        new_node.neighbors = [self.cloneGraph(child) for child in node.neighbors]
        return new_node


# @lc code=end
