class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        v = "aeiouAEIOU"
        n = len(s)
        mid = n // 2
        c = 0
        for i in range(mid):
            if s[i] in v:
                c += 1
            if s[i + mid] in v:
                c -= 1
        return c == 0
