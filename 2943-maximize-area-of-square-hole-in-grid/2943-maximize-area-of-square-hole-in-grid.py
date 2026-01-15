from typing import List

class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        
        def longest_consecutive_length(arr: List[int]) -> int:
            arr.sort()
            longest = 1
            current = 1
            for i in range(1, len(arr)):
                if arr[i] == arr[i - 1] + 1:
                    current += 1
                    longest = max(longest, current)
                else:
                    current = 1
            return longest
        
        # longest run of consecutive horizontal and vertical bars
        horiz = longest_consecutive_length(hBars)
        vert = longest_consecutive_length(vBars)
        
        # side of largest square
        side = min(horiz, vert) + 1
        
        return side * side