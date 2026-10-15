class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = [set() for _ in range(len(board))]
        column = [set() for _ in range(len(board))]
        box = [set() for _ in range(len(board))]
        for r in range(len(board)):
            for c in range(len(board)):
                value = board[r][c]
                if value == ".":
                    continue
                b = (r // 3) * 3 + c // 3
                if value in row[r] or value in column[c] or value in box[b]:
                    return False
                row[r].add(value)
                column[c].add(value)
                box[b].add(value)

        return True