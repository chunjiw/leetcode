# 96. Unique Binary Search Trees
# DescriptionHintsSubmissionsDiscussSolution
# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

# Example:

# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

class Solution(object):
    
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = dict()
        return self.nt(n, table)
    
    def nt(self, n, table):
        if n in table:
            return table[n]
        if n <= 1:
            return 1
        if n == 2:
            return 2
        result = 0
        for i in range(n):
            result += self.nt(i, table) * self.nt(n - i - 1, table)
        table[n] = result
        return result
