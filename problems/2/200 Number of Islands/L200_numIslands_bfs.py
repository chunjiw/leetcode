# 200. Number of Islands

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3

from collections import deque

class Solution(object):
  def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid or not grid[0]:
      return 0
    
    count = 0
    queue = deque()
    popped = set()
    for ii in range(len(grid)):
      for jj in range(len(grid[0])):
        if grid[ii][jj] == '0' or (ii,jj) in popped:
          continue
        queue.append((ii,jj))
        while queue:
          i, j = queue.popleft()
          if (i, j) in popped:
            continue
          if grid[i][j] == '0':
            continue
          popped.add((i,j))
          if i > 0:
            queue.append((i-1, j))
          if j > 0:
            queue.append((i, j-1))
          if i + 1 < len(grid):
            queue.append((i+1, j))
          if j + 1 < len(grid[0]):
            queue.append((i, j+1))
        count += 1
    return count