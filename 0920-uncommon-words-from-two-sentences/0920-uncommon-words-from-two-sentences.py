from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        cnt = {}
        for w in s1.split():
            cnt[w] = cnt.get(w, 0) + 1
        for w in s2.split():
            cnt[w] = cnt.get(w, 0) + 1
        res = []
        for w, v in cnt.items():
            if v == 1:
                res.append(w)
        return res
