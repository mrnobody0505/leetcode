class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        m = len(grid)
        n = len(grid[0])
        INF = 2147483647
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append([(i, j), 0])
                    visited.add((i, j))
        
        while q:
            (i, j), level = q.popleft()
            if i - 1 >= 0 and (i - 1, j) not in visited and grid[i - 1][j] == INF:
                grid[i - 1][j] = level + 1
                q.append([(i - 1, j), level + 1])
                visited.add((i - 1, j))
            if i + 1 < m and (i + 1, j) not in visited and grid[i + 1][j] == INF:
                grid[i + 1][j] = level + 1
                q.append([(i + 1, j), level + 1])
                visited.add((i + 1, j))
            if j - 1 >= 0 and (i, j - 1) not in visited and grid[i][j - 1] == INF:
                grid[i][j - 1] = level + 1
                q.append([(i, j - 1), level + 1])
                visited.add((i, j - 1))
            if j + 1 < n and (i, j + 1) not in visited and grid[i][j + 1] == INF:
                grid[i][j + 1] = level + 1
                q.append([(i, j + 1), level + 1])
                visited.add((i, j + 1))

        

        