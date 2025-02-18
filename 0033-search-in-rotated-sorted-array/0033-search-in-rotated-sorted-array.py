from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # Set search boundaries
        
        while left <= right:
            mid = (left + right) // 2  # Find middle index
            
            if nums[mid] == target:  # Check if mid is the target
                return mid
            
            # Check which half is sorted
            if nums[left] <= nums[mid]:  # Left half is sorted
                if nums[left] <= target < nums[mid]:  # Target in left half
                    right = mid - 1
                else:  # Target in right half
                    left = mid + 1
            else:  # Right half is sorted
                if nums[mid] < target <= nums[right]:  # Target in right half
                    left = mid + 1
                else:  # Target in left half
                    right = mid - 1
        
        return -1  # Target not found
