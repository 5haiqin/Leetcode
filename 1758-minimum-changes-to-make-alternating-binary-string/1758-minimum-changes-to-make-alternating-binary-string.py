class Solution:
    def minOperations(self, s: str) -> int:
        diff1 = 0
        diff2 = 0
        
        for i, ch in enumerate(s):
            if i % 2 == 0:
                if ch != '0':
                    diff1 += 1
                if ch != '1':
                    diff2 += 1
            else:
                if ch != '1':
                    diff1 += 1
                if ch != '0':
                    diff2 += 1
        
        return min(diff1, diff2)