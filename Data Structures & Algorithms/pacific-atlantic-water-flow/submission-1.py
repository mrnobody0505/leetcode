class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        pacifics = set()
        atlantics = set()
        for r in range(ROWS):
            pacifics.add((r, 0))
            atlantics.add((r, COLS - 1))
        for c in range(COLS):
            pacifics.add((0, c))
            atlantics.add((ROWS - 1, c))
        q = deque()
        q.extend(pacifics)
        while q:
            tempr, tempc = q.popleft()
            for dr, dc in directions:
                nextr, nextc = tempr + dr, tempc + dc
                if 0 <= nextr and nextr < ROWS and 0 <= nextc and nextc < COLS and heights[nextr][nextc] >= heights[tempr][tempc] and (nextr, nextc) not in pacifics:
                    pacifics.add((nextr, nextc))
                    q.append((nextr, nextc))

        q.extend(atlantics)
        while q:
            tempr, tempc = q.popleft()
            for dr, dc in directions:
                nextr, nextc = tempr + dr, tempc + dc
                if 0 <= nextr and nextr < ROWS and 0 <= nextc and nextc < COLS and heights[nextr][nextc] >= heights[tempr][tempc] and (nextr, nextc) not in atlantics:
                    atlantics.add((nextr, nextc))
                    q.append((nextr, nextc))
        
        return list(atlantics & pacifics)

        


        

        