# 25. Reverse Nodes in k-Group
# DescriptionHintsSubmissionsDiscussSolution
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

# Example:

# Given this linked list: 1->2->3->4->5

# For k = 2, you should return: 2->1->4->3->5

# For k = 3, you should return: 3->2->1->4->5

# Note:

# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head       
        
        fakehead = ListNode(0)
        fakehead.next = head
        
        pre = fakehead
        
        while True:
            if not head:
                return fakehead.next
            node = head
            for _ in range(k - 1):
                if node.next:
                    node = node.next
                else:
                    return fakehead.next
            tail = node
            next_head = tail.next
            ### the job here is to reverse between head and tail
            curr = head
            post = head.next
            post2 = post.next
            for _ in range(k - 1):
                post.next = curr
                curr = post
                post = post2
                if post:
                    post2 = post.next
            ###
            # link head and tail
            pre.next = tail
            head.next = next_head
            # prepare for next k group
            pre = head
            head = next_head
            
        
