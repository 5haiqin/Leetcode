class Solution:
    def reorderSpaces(self, text: str) -> str:
        s = text.count(" ")
        w = text.split()
        if len(w) == 1:
            return w[0] + " " * s
        gaps = len(w) - 1
        d, r = divmod(s, gaps)
        return (" " * d).join(w) + " " * r
