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
                    q.append((r, c))
                if grid[r][c] == 1:
                    num_fresh += 1

        if num_fresh == 0:
            return 0
        while q:
            for _ in range(len(q)):   
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        num_fresh -= 1
                        q.append((nr, nc))
            minutes += 1        
        if num_fresh > 0:
            return -1
        
        return minutes - 1
        
        
        