class Solution:
    def shortestCompletingWord(self, lp: str, ws: List[str]) -> str:
        from collections import Counter
        req = Counter(c.lower() for c in lp if c.isalpha())
        ans = None
        for w in ws:
            c = Counter(w)
            if all(c[ch] >= req[ch] for ch in req):
                if ans is None or len(w) < len(ans):
                    ans = w
        return ans
