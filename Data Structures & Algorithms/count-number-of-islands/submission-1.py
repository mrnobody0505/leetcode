class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    queue.append((r, c))
                    while queue:
                        top_r, top_c = queue.popleft()
                        grid[top_r][top_c] = "0"
                        for dir_r, dir_c in directions:
                            temp_r, temp_c = top_r + dir_r, top_c + dir_c
                            if 0 <= temp_r and temp_r < ROWS and 0 <= temp_c and temp_c < COLS and grid[temp_r][temp_c] == "1":
                                queue.append((temp_r, temp_c))
                    
                    islands += 1
        
        return islands

            

        
        