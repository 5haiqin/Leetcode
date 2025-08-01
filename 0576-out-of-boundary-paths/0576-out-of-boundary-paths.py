class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        from functools import lru_cache

        @lru_cache(None)
        def dp(i, j, moves):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 1
            if moves == 0:
                return 0
            res = 0
            res += dp(i + 1, j, moves - 1)
            res += dp(i - 1, j, moves - 1)
            res += dp(i, j + 1, moves - 1)
            res += dp(i, j - 1, moves - 1)
            return res % MOD

        return dp(startRow, startColumn, maxMove)
