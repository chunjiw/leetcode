from typing import List
from collections import deque

class Solution:

    def neighbors(self, r, c, m, n):
        result = []
        for i, j in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
            if 0 <= i < m and 0 <= j < n:
                result.append((i, j))
        return result

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        frontier = deque([])
        visited = set()
        top, bot, lef, rit = 0, m-1, 0, n-1
        for j in range(lef, rit+1):
            visited.add((top,j))
            if board[top][j] == 'O':
                frontier.append((top, j))
                board[top][j] = 'Q'
        for i in range(top+1, bot+1):
            visited.add((i,rit))
            if board[i][rit] == 'O':
                frontier.append((i, rit))
                board[i][rit] = 'Q'
        if top < bot:
            visited.add((bot,j))
            for j in range(lef, rit):
                if board[bot][j] == 'O':
                    frontier.append((bot, j))
                    board[bot][j] = 'Q'
        if lef < rit:
            visited.add((i,lef))
            for i in range(top+1, bot):
                if board[i][lef] == 'O':
                    frontier.append((i, lef))
                    board[i][lef] = 'Q'
        while frontier:
            print(frontier)
            for _ in range(len(frontier)):
                i, j = frontier.popleft()
                for ii, jj in self.neighbors(i, j, m, n):
                    if (ii,jj) in visited:
                        continue
                    visited.add((ii,jj))
                    if board[ii][jj] == 'O':
                        frontier.append((ii,jj))
                        board[ii][jj] = 'Q'
        for i in range(m):
            for j in range(n):
                board[i][j] = 'O' if board[i][j] == 'Q' else 'X'

sol = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
sol.solve(board)
print(board)