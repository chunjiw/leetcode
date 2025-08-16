# 51. N-Queens
# DescriptionHintsSubmissionsDiscussSolution
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

# Example:

# Input: 4
# Output: [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        col, minus, plus = set(), set(), set()
        result, solution = [], []
        temp = ['.'] * n
        self.placeQueen(0, solution, col, minus, plus, result, n, temp)
        return result
    
    def placeQueen(self, i, solution, col, minus, plus, result, n, temp):
        if i == n:
            result.append(list(solution))
        for j in range(n):
            if j not in col and i + j not in plus and i - j not in minus:  
                temp[j] = 'Q'
                solution.append(''.join(temp))
                temp[j] = '.'
                col.add(j)
                minus.add(i - j)
                plus.add(i + j)
                self.placeQueen(i + 1, solution, col, minus, plus, result, n, temp)
                solution.pop()
                col.remove(j)
                minus.remove(i - j)
                plus.remove(i + j)
