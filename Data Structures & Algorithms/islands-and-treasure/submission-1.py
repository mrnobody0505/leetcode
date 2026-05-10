class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # visited = {}
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
        while q:
            r, c, level = q.popleft()
            for r_dir, c_dir in directions:
                n_r, n_c = r + r_dir, c + c_dir
                if 0 <= n_r and n_r < ROWS and 0 <= n_c and n_c < COLS and grid[n_r][n_c] == INF:
                    grid[n_r][n_c] = level + 1
                    q.append((n_r, n_c, level + 1))
        



        