from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the array to make it easier to use two-pointer approach
        nums.sort()
        closest_sum = float('inf')  # Initialize with a large number
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1  # Two-pointer approach
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Update closest_sum if the current sum is closer to target
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
                
                # Move pointers to try to get closer to the target
                if current_sum < target:
                    left += 1  # Increase the sum
                elif current_sum > target:
                    right -= 1  # Decrease the sum
                else:
                    return current_sum  # Exact match found
        
        return closest_sum
