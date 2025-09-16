from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = Counter(words[0])
        for w in words[1:]:
            cnt &= Counter(w)
        return list(cnt.elements())
