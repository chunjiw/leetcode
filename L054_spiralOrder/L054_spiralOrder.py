# 54. Spiral Matrix
# DescriptionHintsSubmissionsDiscussSolution
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# Example 1:

# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:

# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        result = []
        m, n = len(matrix), len(matrix[0])
        
        self.traverse(matrix, 0, m, n, result)
        return result
    
    def traverse(self, matrix, si, m, n, result):
        
        
        if m <= n and m % 2 and si == m / 2:
            for i in range(si, n - si):
                result.append(matrix[si][i])
            return
        if n <= m and n % 2 and si == n / 2:
            for i in range(si, m - si):
                result.append(matrix[i][si])
            return
                
        if si >= min(n, m) / 2:
            return
        
        for i in range(si, n - si - 1):
            result.append(matrix[si][i])
            
        for i in range(si, m - si - 1):
            result.append(matrix[i][n - si - 1])
    
        for i in range(n - si - 1, si, -1):
            result.append(matrix[m - si - 1][i])
            
        for i in range(m - si - 1, si, -1):
            result.append(matrix[i][si])
        
        self.traverse(matrix, si + 1, m, n, result)
