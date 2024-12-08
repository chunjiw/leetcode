# 417. Pacific Atlantic Water Flow

# Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

# Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

# Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

# Note:
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
# Example:

# Given the following 5x5 matrix:

#   Pacific ~   ~   ~   ~   ~ 
#        ~  1   2   2   3  (5) *
#        ~  3   2   3  (4) (4) *
#        ~  2   4  (5)  3   1  *
#        ~ (6) (7)  1   4   5  *
#        ~ (5)  1   1   2   4  *
#           *   *   *   *   * Atlantic

# Return:

# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).


class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        # Depth first search
        if not matrix:
            return []
        M, N = len(matrix), len(matrix[0])
        if not M or not N:
            return []

        result = []
        can1 = [[False for _ in range(N)] for _ in range(M)]
        can2 = [[False for _ in range(N)] for _ in range(M)]
        visited1 = [[False for _ in range(N)] for _ in range(M)]
        visited2 = [[False for _ in range(N)] for _ in range(M)]

        # initial condition
        for j in range(N):
            can1[0][j] = True
            visited1[0][j] = True
            can2[M - 1][j] = True
            visited2[M - 1][j] = True
            
        for i in range(M):
            can1[i][0] = True
            visited1[i][0] = True
            can2[i][N - 1] = True
            visited2[i][N - 1] = True

        for i in range(M):
            for j in range(N):
                if not visited1[i][j]:
                    self.visit(i, j, M, N, matrix, visited1, can1)
                if not visited2[i][j]:
                    self.visit(i, j, M, N, matrix, visited2, can2)

        for i in range(M):
            for j in range(N):
                if can1[i][j] and can2[i][j]:
                    result.append([i, j])

        return result

    def visit(self, i, j, M, N, matrix, visited, can):
        if visited[i][j]:
            return
        visited[i][j] = True
        for ni, nj in self.neighbors(i, j, M, N):
            if matrix[i][j] >= matrix[ni][nj]:
                self.visit(ni, nj, M, N, matrix, visited, can)
                if can[ni][nj]:
                    can[i][j] = True
                    # deal with equal height situation
                    for ii, jj in self.neighbors(i, j, M, N):
                        if matrix[i][j] <= matrix[ii][jj]:
                            can[ii][jj] = True
                    return
                
    
    def neighbors(self, i, j, M, N):
        result = []
        if j - 1 >= 0:
            result.append((i, j - 1))
        if j + 1 < N:
            result.append((i, j + 1))
        if i - 1 >= 0:
            result.append((i - 1, j))
        if i + 1 < M:
            result.append((i + 1, j))
        return result






