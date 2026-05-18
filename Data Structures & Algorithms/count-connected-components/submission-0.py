class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjlist = {}
        for edge in edges:
            u, v = edge
            adjlist[u] = adjlist.get(u, [])
            adjlist[v] = adjlist.get(v, [])
            adjlist[u].append(v)
            adjlist[v].append(u)     
        cnt = 0
        visited = set()
        no_component = 0
        def dfs(v):
            nonlocal cnt
            if v in visited:
                return
            visited.add(v)
            cnt += 1
            adjlist[v] = adjlist.get(v, [])
            for n in adjlist[v]:
                dfs(n)
            return
        
        while cnt != n:
            for i in range(n):
                if i not in visited:
                    dfs(i)
                    no_component += 1
        
        return no_component




        