class Solution:
    def reverseWords(self, s: str) -> str:
        w = s.split()
        w.reverse()
        return " ".join(w)
