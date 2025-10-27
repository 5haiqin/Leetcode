class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = 0
        bal = 0
        for c in s:
            if c == 'L':
                bal += 1
            else:
                bal -= 1
            if bal == 0:
                cnt += 1
        return cnt
