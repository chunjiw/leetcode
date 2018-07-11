# 23. Merge k Sorted Lists
# DescriptionHintsSubmissionsDiscussSolution
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Example:

# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # run time O(n*k*log(k))
        
        from heapq import heappush, heappop
        
        fakehead = ListNode(0)
        current = fakehead
        
        front = []
        for head in lists:
            if head:
                heappush(front, (head.val, head))
        while front:
            top = heappop(front)[1]
            current.next = top
            current = current.next
            if top.next:
                heappush(front, (top.next.val, top.next))
        
        return fakehead.next
