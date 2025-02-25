from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0  # Count jumps
        farthest = 0  # Farthest we can reach
        end = 0  # End of the current jump range
        
        for i in range(n - 1):  # Don't need to jump from last index
            farthest = max(farthest, i + nums[i])  # Update farthest reach
            
            if i == end:  # If reached the end of current jump
                jumps += 1  # Make a jump
                end = farthest  # Update end to the farthest reached
                
        return jumps
