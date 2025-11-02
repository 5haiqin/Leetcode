class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for w in words:
            for t in words:
                if w != t and w in t:
                    res.append(w)
                    break
        return res
