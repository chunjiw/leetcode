from typing import List
from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        root = ''.join([str(n) for row in board for n in row])
        target = '123450'
        
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [3, 1, 5],
            5: [4, 2],
        }
        
        line = deque([root])
        visited = {root}
        steps = 0
        while line:
            for _ in range(len(line)):
                board = line.popleft()
                if board == target:
                    return steps
                index = board.index('0')
                for nei in neighbors[index]:
                    nb = list(board)
                    nb[index] = nb[nei]
                    nb[nei] = '0'
                    nb = ''.join(nb)
                    if nb not in visited:
                        visited.add(nb)
                        line.append(nb)
            steps += 1
        return -1

sol = Solution()
print(sol.slidingPuzzle([[1,2,3],[4,0,5]]))
print(sol.slidingPuzzle([[1,2,3],[5,4,0]]))
print(sol.slidingPuzzle([[4,1,2],[5,0,3]]))

