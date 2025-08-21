class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        cur = 0
        for c in s:
            w = widths[ord(c) - ord('a')]
            if cur + w <= 100:
                cur += w
            else:
                lines += 1
                cur = w
        return [lines, cur]
