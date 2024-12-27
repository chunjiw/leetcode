class Solution:

    def neighbors(self, m, n, i, j):
        result = []
        for ii, jj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= ii < m and 0 <= jj < n:
                result.append((ii, jj))
        return result

    def search(self, i, j, k, board, word):
        m = len(board)
        n = len(board[0])
        if (i, j) in self.path or k >= len(word) or board[i][j] != word[k]:
            return
        if k == len(word) - 1 and board[i][j] == word[k]:
            self.result = True
            return
        self.path.add((i,j))
        for ii, jj in self.neighbors(m, n, i, j):
            self.search(ii, jj, k + 1, board, word)
        self.path.remove((i,j))

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        self.result = False
        for i in range(m):
            for j in range(n):
                self.path = set()
                self.search(i, j, 0, board, word)
                if self.result:
                    return self.result
        return self.result
