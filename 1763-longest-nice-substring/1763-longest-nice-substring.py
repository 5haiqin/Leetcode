class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(t: str) -> bool:
            st = set(t)
            for ch in st:
                if ch.lower() not in st or ch.upper() not in st:
                    return False
            return True

        n = len(s)
        best = ""
        for i in range(n):
            for j in range(i, n):
                cur = s[i:j+1]
                if len(cur) > len(best) and is_nice(cur):
                    best = cur
        return best
