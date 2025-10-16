from typing import List

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        n = len(s)
        i = 0
        res = []
        for j in range(1, n + 1):
            if j == n or s[j] != s[j - 1]:
                if j - i >= 3:
                    res.append([i, j - 1])
                i = j
        return res
