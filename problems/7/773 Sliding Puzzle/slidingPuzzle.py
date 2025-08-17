from typing import List
from collections import deque
from copy import deepcopy

class Solution:

    def toNum(self, board):
        res = 0
        for row in board:
            for num in row:
                res *= 10
                res += num
        return res

    def getNeis(self, board):
        m, n = len(board), len(board[0])
        result = []
        for r in range(m):
            for c in range(n):
                if board[r][c] == 0:
                    if c - 1 >= 0:
                        clone = deepcopy(board)
                        clone[r][c-1], clone[r][c] = clone[r][c], clone[r][c-1]
                        result.append(clone)
                    if c + 1 < n:
                        clone = deepcopy(board)
                        clone[r][c+1], clone[r][c] = clone[r][c], clone[r][c+1]
                        result.append(clone)
                    clone = deepcopy(board)
                    clone[1-r][c], clone[r][c] = clone[r][c], clone[1-r][c]
                    result.append(clone)
        return result
                    
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        num = self.toNum(board)
        if num == 123450:
            return 0
        line = deque([board])
        visited = set()
        visited.add(num)
        steps = 1
        while line:
            for _ in range(len(line)):
                board = line.popleft()
                for nei in self.getNeis(board):
                    num = self.toNum(nei)
                    if num == 123450:
                        return steps
                    if num not in visited:
                        visited.add(num)
                        line.append(nei)
            steps += 1
        return -1


sol = Solution()
print(sol.slidingPuzzle([[1,2,3],[4,0,5]]))
print(sol.slidingPuzzle([[1,2,3],[5,4,0]]))
print(sol.slidingPuzzle([[4,1,2],[5,0,3]]))

