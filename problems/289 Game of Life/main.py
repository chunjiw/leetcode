class Solution:
    def status(self, board, i, j):
        result = 0
        for r, c in [(ii, jj) for ii in (i-1, i, i+1) for jj in range(j-1, j+2) if i != ii or j != jj]:
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] % 2:
                result += 1
        return board[i][j] % 2, result

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                live, nnei = self.status(board, i, j)
                if (live and 2 <= nnei <=3) or (not live and nnei == 3):
                    board[i][j] += 2
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] //= 2
