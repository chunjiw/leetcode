class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def get_successor(node):
    """Assumes successor exists"""
    node = node.right
    while node.left:
        node = node.left
    return node

def insert(num, node, valueDiff):
    """Assumes node is not None"""
    if num + valueDiff < node.val:
        if node.left:
            return insert(num, node.left, valueDiff)
        else:
            node.left = Node(num)
            return True
    elif num - valueDiff > node.val:
        if node.right:
            return insert(num, node.right, valueDiff)
        else:
            node.right = Node(num)
            return True
    else:
        return False

def delete(num, node):
    if not node:
        return node
    if num < node.val:
        node.left = delete(num, node.left)
    elif num > node.val:
        node.right = delete(num, node.right)
    else:
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        successor = get_successor(node)
        node.val = successor.val
        node.right = delete(successor.val, node.right)
    return node

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        k = indexDiff + 1
        root = Node(nums[0])
        for i in range(1, len(nums)):
            if i >= k:
                root = delete(nums[i-k], root)
            if not insert(nums[i], root, valueDiff):
                return True
        return False
