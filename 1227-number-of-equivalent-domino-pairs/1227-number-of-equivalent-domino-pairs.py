class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cnt = {}
        ans = 0
        for a, b in dominoes:
            key = a * 10 + b if a < b else b * 10 + a
            ans += cnt.get(key, 0)
            cnt[key] = cnt.get(key, 0) + 1
        return ans
