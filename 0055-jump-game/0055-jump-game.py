from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0  # Max index we can reach
        
        for i, num in enumerate(nums):
            if i > max_reach:
                return False  # If current index is unreachable
            
            max_reach = max(max_reach, i + num)  # Update max reach
            
            if max_reach >= len(nums) - 1:
                return True  # If we can reach the last index
        
        return False  # If we exit loop without reaching the end
