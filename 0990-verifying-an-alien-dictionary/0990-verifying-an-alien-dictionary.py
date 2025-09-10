class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        m = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for c1, c2 in zip(w1, w2):
                if m[c1] < m[c2]:
                    break
                if m[c1] > m[c2]:
                    return False
            else:
                if len(w1) > len(w2):
                    return False
        return True
