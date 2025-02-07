from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0  # Left pointer
        right = len(height) - 1  # Right pointer
        max_water = 0  # To store the maximum water
        while left < right:
            # Calculate the area
            width = right - left
            min_height = min(height[left], height[right])
            area = width * min_height
            # Update max_water if we found a larger area
            max_water = max(max_water, area)
            # Move the pointer pointing to the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water
