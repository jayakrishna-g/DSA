#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def createNode(self, val, prev):
        cur = ListNode(val % 10)
        prev.next = cur
        return cur, val // 10

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0
        prev = ListNode()
        head = prev
        while l1 and l2:
            s = l1.val + l2.val + carry
            prev, carry = self.createNode(s, prev)
            l1 = l1.next
            l2 = l2.next

        while l1:
            s = l1.val + carry
            prev, carry = self.createNode(s, prev)
            l1 = l1.next

        while l2:
            s = l2.val + carry
            prev, carry = self.createNode(s, prev)
            l2 = l2.next

        while carry > 0:
            prev, carry = self.createNode(carry, prev)

        return head.next


# @lc code=end
