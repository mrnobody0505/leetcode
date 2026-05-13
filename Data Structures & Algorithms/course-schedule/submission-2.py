class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_list = [[] for _ in range(numCourses)]
        visited = set()
        for mod, prereq_mod in prerequisites:
            prereq_list[mod].append(prereq_mod)
        # print(prereq_list)
        def dfs(mod):
            if mod in visited:
                return False
            if not prereq_list[mod]:
                return True
            visited.add(mod)
            # print(mod)
            for prereq_mod in prereq_list[mod]:
                if not dfs(prereq_mod):
                    return False
            visited.remove(mod)
            prereq_list[mod] = []
            return True
            
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

        