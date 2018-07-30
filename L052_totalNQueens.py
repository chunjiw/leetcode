# 52. N-Queens II
# DescriptionHintsSubmissionsDiscussSolution
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



# Given an integer n, return the number of distinct solutions to the n-queens puzzle.

# Example:

# Input: 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        # solution representation
        # list of length n 
        col, minus, plus = set(), set(), set()
        count = [0]
        self.placeQueen(0, col, minus, plus, count, n)
        return count[0]
    
    def placeQueen(self, i, col, minus, plus, count, n):
        if i == n:
            count[0] += 1
        for j in range(n):
            if j not in col and i + j not in plus and i - j not in minus:           
                col.add(j)
                minus.add(i - j)
                plus.add(i + j)
                self.placeQueen(i + 1, col, minus, plus, count, n)
                col.remove(j)
                minus.remove(i - j)
                plus.remove(i + j)
            
        
        
        
