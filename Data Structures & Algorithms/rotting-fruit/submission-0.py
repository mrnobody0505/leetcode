class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        minutes = 0
        num_fresh = 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                if grid[r][c] == 1:
                    num_fresh += 1
        
        while q:
            r, c, level = q.popleft()
            for dir_r, dir_c in directions:
                nr, nc = r + dir_r, c + dir_c
                if 0 <= nr and nr < ROWS and 0 <= nc and nc < COLS and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    num_fresh -= 1
                    q.append((nr, nc, level + 1))
                    minutes = level + 1
        
        if num_fresh > 0:
            return -1
        
        return minutes
        
        
        