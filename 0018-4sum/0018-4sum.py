from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Sort the array to handle duplicates easily
        nums.sort()
        n = len(nums)
        result = []
        
        # Fix the first element
        for i in range(n - 3):
            # Avoid duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Fix the second element
            for j in range(i + 1, n - 2):
                # Avoid duplicate second elements
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Two-pointer approach for the remaining two elements
                left, right = j + 1, n - 1
                while left < right:
                    four_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if four_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Move left and right to avoid duplicates
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        left += 1
                        right -= 1
                    elif four_sum < target:
                        left += 1  # Increase sum
                    else:
                        right -= 1  # Decrease sum
        
        return result
