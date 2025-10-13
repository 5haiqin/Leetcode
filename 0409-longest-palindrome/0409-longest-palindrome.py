from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        res = 0
        odd = 0
        for v in c.values():
            res += (v // 2) * 2
            if v % 2:
                odd = 1
        return res + odd
