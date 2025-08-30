class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        blks = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                num = int(num)
                k = i // 3 * 3 + j // 3
                if num in rows[i] or num in cols[j] or num in blks[k]:
                    return False
                rows[i].add(num)
                cols[j].add(num)
                blks[k].add(num)
        return True