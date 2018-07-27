# 289. Game of Life
# DescriptionHintsSubmissionsDiscussSolution
# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

# Example:

# Input: 
# [
#   [0,1,0],
#   [0,0,1],
#   [1,1,1],
#   [0,0,0]
# ]
# Output: 
# [
#   [0,0,0],
#   [1,0,1],
#   [0,1,1],
#   [0,1,0]
# ]
# Follow up:

# Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return board
        for i in range(len(board)):
            for j in range(len(board[0])):
                neighbors = 0
                for ii in range(-1, 2):
                    for jj in range(-1, 2):
                        if not (ii == 0 and jj == 0):
                            neighbors += self.get(board, i + ii, j + jj)
                if self.get(board, i, j) == 0:
                    if neighbors == 3:    # 0 -> 1
                        board[i][j] = 5
                    else:                   # 0 -> 0
                        board[i][j] = 6
                else:
                    if neighbors < 2 or neighbors > 3:
                        board[i][j] = 8     # 1 -> 0
                    else:
                        board[i][j] = 7     # 1 -> 1
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = board[i][j] % 2
        return

    def get(self, board, i, j):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return 0
        else:
            if board[i][j] < 3:
                return board[i][j]
            if board[i][j] <= 6:
                return 0
            else:
                return 1 