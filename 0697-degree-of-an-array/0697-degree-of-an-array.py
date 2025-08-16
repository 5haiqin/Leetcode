from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        first = {}
        last = {}
        
        for i, x in enumerate(nums):
            if x not in first:
                first[x] = i
            last[x] = i
            counts[x] += 1
        
        degree = max(counts.values())
        min_len = len(nums)
        
        for x, cnt in counts.items():
            if cnt == degree:
                length = last[x] - first[x] + 1
                if length < min_len:
                    min_len = length
        
        return min_len
