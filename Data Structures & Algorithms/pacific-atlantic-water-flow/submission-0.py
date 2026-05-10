class Solution:
    def pacificAtlantic(self, heights):
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        def bfs(starts):
            q = deque(starts)
            visited = set(starts)
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr,nc) not in visited and heights[nr][nc] >= heights[r][c]:
                        visited.add((nr, nc))
                        q.append((nr, nc))
            return visited

        pacific_starts = [(r,0) for r in range(ROWS)] + [(0,c) for c in range(COLS)]
        atlantic_starts = [(r,COLS-1) for r in range(ROWS)] + [(ROWS-1,c) for c in range(COLS)]

        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)

        return list(pacific & atlantic)