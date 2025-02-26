from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []  # Store all permutations
        
        def backtrack(path, options):
            if not options:  # If no more numbers left, add to result
                result.append(path)
                return
            
            for i in range(len(options)):
                backtrack(path + [options[i]], options[:i] + options[i+1:])
                
        backtrack([], nums)  # Start backtracking
        return result
