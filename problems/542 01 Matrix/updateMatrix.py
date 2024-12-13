# 542. 01 Matrix

# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.
# Example 1: 
# Input:

# 0 0 0
# 0 1 0
# 0 0 0
# Output:
# 0 0 0
# 0 1 0
# 0 0 0
# Example 2: 
# Input:

# 0 0 0
# 0 1 0
# 1 1 1
# Output:
# 0 0 0
# 0 1 0
# 1 2 1
# Note:
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []

        M, N = len(matrix), len(matrix[0])
        visited = set()
        # initial condition
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    visited.add(i * N + j)
        border = list(visited)
        dis = 1
        while border:
            newborder = []
            for k in border:
                for nk in self.neighbors(k, M, N):
                    if nk not in visited:
                        visited.add(nk)
                        matrix[nk / N][nk % N] = dis
                        newborder.append(nk)
            border = newborder
            dis += 1
        return matrix

    def neighbors(self, k, M, N):
        i, j = k / N, k % N
        nei = []
        if i - 1 >= 0:
            nei.append(k - N)
        if i + 1 < M:
            nei.append(k + N)
        if j - 1 >= 0:
            nei.append(k - 1)
        if j + 1 < N:
            nei.append(k + 1)
        return nei