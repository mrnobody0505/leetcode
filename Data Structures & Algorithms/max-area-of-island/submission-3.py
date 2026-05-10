class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])
        ans = 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    q.append((r, c))
                    grid[r][c] = 0
                    area = 0
                    while q:
                        top_r, top_c = q.popleft()
                        area += 1
                        for r_dir, c_dir in directions:
                            temp_r, temp_c = top_r + r_dir, top_c + c_dir
                            if 0 <= temp_r and temp_r < ROWS and 0 <= temp_c and temp_c < COLS and grid[temp_r][temp_c] == 1:
                                grid[temp_r][temp_c] = 0
                                q.append((temp_r, temp_c))
                    
                    ans = max(ans, area)
        
        return ans

        