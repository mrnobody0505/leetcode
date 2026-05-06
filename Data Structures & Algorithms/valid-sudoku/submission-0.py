class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in board:
            s = set()
            for c in r:
                if c == ".":
                    continue
                if c in s:
                    return False
                s.add(c)
        
        for i in range(len(board)):
            s = set()
            for row in board:
                if row[i] == ".":
                    continue
                if row[i] in s:
                    return False
                s.add(row[i])
        
        for r in range(0, len(board), 3):
            for c in range(0, len(board), 3):
                s = set()
                for i in range(3):
                    for j in range(3):
                        if board[r + i][c + j] == ".":
                            continue
                        if board[r + i][c + j] in s:
                            return False
                        s.add(board[r + i][c + j])
        
        return True




        
        