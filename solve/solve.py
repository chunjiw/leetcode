#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 130. Surrounded Regions

# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Example:

# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:

# X X X X
# X X X X
# X X X X
# X O X X
# Explanation:

# Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        visited = set()
        M = len(board)
        N = len(board[0])
        for i in range(0, M * N):
            if board[i / N][i % N] == 'O' and i not in visited:
                visited.add(i)
                island = set()
                self.chart(board, i, M, N, island, visited)
                if self.surrounded(board, island, M, N):
                    self.flip(board, island, N)
        return

    def chart(self, board, i, M, N, indexes, visited):
        # chart the indexes of an island
        if i < 0 or i >= M * N or i in indexes or board[i / N][i % N] == 'X':
            return
        else:
            indexes.add(i)
            visited.add(i)
            self.chart(board, i + 1, M, N, indexes, visited)
            self.chart(board, i - 1, M, N, indexes, visited)
            self.chart(board, i + N, M, N, indexes, visited)
            self.chart(board, i - N, M, N, indexes, visited)
        return

    def surrounded(self, board, indexes, M, N):
        # check an island is surrounded or not
        for i in indexes:
            if (i / N == 0) or (i / N == M - 1) or (i % N == 0) or (i % N == N - 1):
                return False
        return True
        
    def flip(self, board, indexes, N):
        # flip at indexes
        for i in indexes:
            board[i / N][i % N] = 'X'
        return



