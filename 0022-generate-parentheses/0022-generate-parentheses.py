from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []  # Store valid combinations
        
        def backtrack(s, open_count, close_count):
            if len(s) == 2 * n:  # Base case: valid sequence
                result.append(s)
                return
            
            if open_count < n:  # Add '(' if possible
                backtrack(s + '(', open_count + 1, close_count)
            
            if close_count < open_count:  # Add ')' if valid
                backtrack(s + ')', open_count, close_count + 1)
        
        backtrack("", 0, 0)
        return result
