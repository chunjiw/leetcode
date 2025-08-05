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
        # Breadth first search, from the ocean
        # Use hashset, so use 1d coordinate
        # i, j -> i * N + j
        # k -> k / N, k % N
        if not matrix:
            return []
        M, N = len(matrix), len(matrix[0])
        if not M or not N:
            return []
        result = []

        territory = [h for row in matrix for h in row]
        water1, visited1 = set(), set()
        water2, visited2 = set(), set()
        
        # initial condition
        for j in range(N):
            water1.add(j)
            water2.add(M * N - N + j)

        for i in range(M):
            water1.add(i * N)
            water2.add(i * N + N - 1)

        border1 = set(water1)
        border2 = set(water2)

        self.permeate(border1, water1, M, N, territory)
        self.permeate(border2, water2, M, N, territory)

        for i in range(M):
            for j in range(N):
                k = i * N + j
                if k in water1 and k in water2:
                    result.append([i, j])
        return result

    def permeate(self, border, water, M, N, territory):
        while border:
            newborder = set()
            for k in border:
                for nk in self.neighbors(k, M, N):
                    if nk not in water:
                        if territory[k] <= territory[nk]:
                            water.add(nk)
                            newborder.add(nk)
            border = newborder
    
    def neighbors(self, k, M, N):
        i, j = k / N, k % N
        result = []
        if j - 1 >= 0:
            result.append(k - 1)
        if j + 1 < N:
            result.append(k + 1)
        if i - 1 >= 0:
            result.append(k - N)
        if i + 1 < M:
            result.append(k + N)
        return result

