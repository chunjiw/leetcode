# 19. Remove Nth Node From End of List
# DescriptionHintsSubmissionsDiscussSolution
# Given a linked list, remove the n-th node from the end of list and return its head.

# Example:

# Given linked list: 1->2->3->4->5, and n = 2.

# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:

# Given n will always be valid.

# Follow up:

# Could you do this in one pass?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n < 1:
            return head
        if not head:
            return head
        last, n1th = head, head
        for i in range(n):
            last = last.next
        # if nth node is head:
        if not last:
            return head.next
        # look for n+1 node
        last = last.next
        while last:
            last = last.next
            n1th = n1th.next
        n1th.next = n1th.next.next
        return head
