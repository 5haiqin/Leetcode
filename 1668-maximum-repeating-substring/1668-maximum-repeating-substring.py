class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if not word or not sequence:
            return 0
        count = 0
        cur = word
        while cur in sequence:
            count += 1
            cur += word
        return count