class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_list = [[] for _ in range(numCourses)]
        for mod, prereq_mod in prerequisites:
            prereq_list[mod].append(prereq_mod)
        
        visited = set()
        mem = {}
        def dfs(mod):
            if mod in visited:
                mem[mod] = []
                return mem[mod]
            if not prereq_list[mod]:
                mem[mod] = [mod] if mod not in mem else mem[mod]
                return mem[mod]
            visited.add(mod)
            ret = []
            for prereq_mod in prereq_list[mod]:
                temp = mem[prereq_mod] if prereq_mod in mem else dfs(prereq_mod)
                if not temp:
                    return []
                ret += temp
            visited.remove(mod)
            ret.append(mod)
            mem[mod] = ret
            prereq_list[mod] = []
            return mem[mod]
        
        ans = []
        added = set()
        for i in range(numCourses):
            temp = dfs(i)
            # print(i, temp)
            if not temp:
                return []
            for m in temp:
                if m not in added:
                    ans.append(m)
                    added.add(m)
        
        return ans


                

        