class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set) 

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".": #dots are placeholders
                    continue    

                b = (r // 3) * 3 + (c // 3)

                if val in rows[r]:
                    return False
                if val in cols[c]:
                    return False
                if val in boxes[b]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[b].add(val)



        return True
        