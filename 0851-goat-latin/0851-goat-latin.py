class Solution:
    def toGoatLatin(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        words = s.split()
        res = []
        for i, w in enumerate(words, start=1):
            if w[0] not in vowels:
                w = w[1:] + w[0]
            w = w + "ma" + ("a" * i)
            res.append(w)
        return " ".join(res)
