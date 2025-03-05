from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]  # Initialize max sum
        curr_sum = 0  # Current sum tracker
        
        for num in nums:
            if curr_sum < 0:
                curr_sum = 0  # Reset if negative
            curr_sum += num  # Add current number
            max_sum = max(max_sum, curr_sum)  # Update max sum
        
        return max_sum
