from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        res = [''] * n
        for i, ch in enumerate(s):
            res[indices[i]] = ch
        return ''.join(res)
