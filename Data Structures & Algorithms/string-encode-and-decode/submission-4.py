class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return '#'
        ecs = ''
        for s in strs:
            ecs += str(len(s)) + ','
        ecs += '#'
        for s in strs:
            ecs += s
        
        return ecs

    def decode(self, s: str) -> List[str]:
        if s == '#':
            return []
        print(s)
        szs = []
        i = 0
        while s[i] != '#':
            sz = ''
            while s[i] != ',':
                sz += s[i]
                i += 1
            szs.append(int(sz))
            i += 1
        i += 1
        dcs = []
        for sz in szs:
            dcs.append(s[i: i + sz])
            i += sz

        return dcs