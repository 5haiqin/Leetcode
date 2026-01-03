class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        abc = 6
        aba = 6

        for _ in range(1, n):
            abc, aba = (abc * 2 + aba * 2) % MOD, (abc * 2 + aba * 3) % MOD

        return (abc + aba) % MOD
