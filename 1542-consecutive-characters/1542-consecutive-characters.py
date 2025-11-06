class Solution:
    def maxPower(self, s: str) -> int:
        if not s:
            return 0
        cur = 1
        best = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 1
        return best
