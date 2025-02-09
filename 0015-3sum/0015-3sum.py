from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []  # To store the triplets
        nums.sort()  # Sort the array to make two-pointer approach possible
        
        for i in range(len(nums) - 2):  # Iterate through the array
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates
                continue
            
            left, right = i + 1, len(nums) - 1  # Two-pointer approach
            while left < right:
                total = nums[i] + nums[left] + nums[right]  # Sum of three numbers
                
                if total == 0:  # If sum is zero, store the triplet
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Move left and right pointers, skipping duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1  # Move left pointer to increase sum
                else:
                    right -= 1  # Move right pointer to decrease sum
        
        return res
