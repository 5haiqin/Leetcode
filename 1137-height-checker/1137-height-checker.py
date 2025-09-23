class Solution:
    def heightChecker(self, h: List[int]) -> int:
        s = sorted(h)
        cnt = 0
        for i in range(len(h)):
            if h[i] != s[i]:
                cnt += 1
        return cnt
