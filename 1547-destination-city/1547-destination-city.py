class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s = set()
        for a, b in paths:
            s.add(a)
        for a, b in paths:
            if b not in s:
                return b
        return ""
