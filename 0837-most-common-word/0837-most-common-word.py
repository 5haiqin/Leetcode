import re
from collections import Counter

class Solution:
    def mostCommonWord(self, p: str, b: list[str]) -> str:
        bset = set(b)
        words = re.findall(r'\w+', p.lower())
        cnt = Counter(w for w in words if w not in bset)
        return cnt.most_common(1)[0][0]
