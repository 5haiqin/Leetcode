from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals based on the start value
        intervals.sort()
        
        merged = []  # Result list
        
        for interval in intervals:
            # If merged list is empty or no overlap, add the interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Merge overlapping intervals
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
