from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index = {num: i for i, num in enumerate(arr)}  # Store indices of numbers
        dp = {}  # Dictionary to store sequence length
        max_len = 0  # Track max sequence length
        
        for k in range(len(arr)):
            for j in range(k):
                i = index.get(arr[k] - arr[j])  # Find previous number
                if i is not None and i < j:  # Check valid sequence
                    dp[j, k] = dp.get((i, j), 2) + 1  # Update sequence length
                    max_len = max(max_len, dp[j, k])  # Update max length
                    
        return max_len if max_len >= 3 else 0  # Return result
