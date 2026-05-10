class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])
        ans = 0
        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            area = 1
            for dir_r, dir_c in directions:
                area += dfs(r + dir_r, c + dir_c)
            
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    ans = max(ans, dfs(r, c))
        
        return ans

        