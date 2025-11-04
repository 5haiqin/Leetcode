class Solution:
    def maxScore(self, s: str) -> int:
        o = s.count("1")
        z = 0
        res = 0
        for i in range(len(s) - 1):
            if s[i] == "0":
                z += 1
            else:
                o -= 1
            if z + o > res:
                res = z + o
        return res
