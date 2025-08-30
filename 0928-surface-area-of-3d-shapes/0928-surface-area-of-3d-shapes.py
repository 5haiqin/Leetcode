class Solution:
    def surfaceArea(self, g: List[List[int]]) -> int:
        n = len(g)
        ans = 0
        for i in range(n):
            for j in range(n):
                v = g[i][j]
                if v:
                    ans += v * 4 + 2
                    if i > 0:
                        ans -= 2 * min(v, g[i - 1][j])
                    if j > 0:
                        ans -= 2 * min(v, g[i][j - 1])
        return ans
