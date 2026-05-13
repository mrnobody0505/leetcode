class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        INF = 2147483647
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        visited = set()
        level = 0
        while q:
            tempr, tempc = q.popleft()
            for dr, dc in directions:
                nextr, nextc = tempr + dr, tempc + dc
                if 0 <= nextr and nextr < ROWS and 0 <= nextc and nextc < COLS and grid[nextr][nextc] == INF:
                    grid[nextr][nextc] = grid[tempr][tempc] + 1
                    q.append((nextr, nextc))



        