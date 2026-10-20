class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                curr = board[r][c]
                if curr==".":
                    continue
                curr_box = r//3*3+c//3
                if curr in rows[r] or curr in cols[c] or curr in boxes[curr_box]:
                    return False
                rows[r].add(curr)
                cols[c].add(curr)
                boxes[curr_box].add(curr)
        return True