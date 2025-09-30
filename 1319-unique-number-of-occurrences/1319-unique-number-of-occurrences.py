from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        freqs = cnt.values()
        return len(freqs) == len(set(freqs))
