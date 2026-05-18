class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        visited = set()
        adjlist = {}
        for edge in edges:
            v1, v2 = edge
            adjlist[v1] = adjlist.get(v1, [])
            adjlist[v2] = adjlist.get(v2, [])
            adjlist[v1].append(v2)
            adjlist[v2].append(v1)
        
        def dfs(v, parent):
            if v in visited:
                return -1
            visited.add(v)
            adjlist[v] = adjlist.get(v, [])
            if not adjlist[v]:
                return 0
            for n in adjlist[v]:
                if n == parent:
                    continue
                if dfs(n, v) == -1:
                    return -1
            return 0
        
        return dfs(0, -1) == 0 and len(visited) == n