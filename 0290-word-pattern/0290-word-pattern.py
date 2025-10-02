class Solution:
    def wordPattern(self, pat: str, s: str) -> bool:
        w = s.split()
        if len(pat) != len(w):
            return False
        m1 = {}  
        m2 = {}  
        for c, word in zip(pat, w):
            if c in m1:
                if m1[c] != word:
                    return False
            else:
                if word in m2:
                    return False
                m1[c] = word
                m2[word] = c
        return True
