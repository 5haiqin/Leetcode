class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jset = set(jewels)
        cnt = 0
        for s in stones:
            if s in jset:
                cnt += 1
        return cnt
