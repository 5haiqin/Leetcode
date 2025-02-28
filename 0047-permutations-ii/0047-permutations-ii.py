from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []  # Store results
        nums.sort()  # Sort to handle duplicates
        
        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path[:])  # Add a copy of path
                return
            
            for i in range(len(nums)):
                if used[i]:  # Skip if already used
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:  
                    continue
                
                used[i] = True
                path.append(nums[i])
                backtrack(path, used)
                path.pop()
                used[i] = False
        
        backtrack([], [False] * len(nums))
        return res