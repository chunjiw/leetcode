from typing import List
from collections import deque

class Solution:

    def neighbors(self, r, c, m, n):
        result = []
        for i, j in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
            if 0 <= i < m and 0 <= j < n:
                result.append((i, j))
        return result

    def process(self, ii, jj, board, frontier, visited):
        if (ii,jj) in visited:
            return
        visited.add((ii,jj))
        if board[ii][jj] == 'O':
            frontier.append((ii,jj))
            board[ii][jj] = 'Q'        

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        frontier = deque([])
        visited = set()
        top, bot, lef, rit = 0, m-1, 0, n-1
        for j in range(lef, rit+1):
            self.process(top, j, board, frontier, visited)
        for i in range(top+1, bot+1):
            self.process(i, rit, board, frontier, visited)
        if top < bot:
            for j in range(lef, rit):
                self.process(bot, j, board, frontier, visited)
        if lef < rit:
            for i in range(top+1, bot):
                self.process(i, lef, board, frontier, visited)
        while frontier:
            for _ in range(len(frontier)):
                i, j = frontier.popleft()
                for ii, jj in self.neighbors(i, j, m, n):
                    self.process(ii, jj, board, frontier, visited)
        for i in range(m):
            for j in range(n):
                board[i][j] = 'O' if board[i][j] == 'Q' else 'X'

sol = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
sol.solve(board)
print(board)