from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Mapping of digits to letters like a phone keypad
        digit_to_letters = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        # If input is empty, return an empty list
        if not digits:
            return []
        
        # Function to generate combinations using backtracking
        def backtrack(index, path):
            # If we have a combination of the same length as digits, add to result
            if index == len(digits):
                combinations.append("".join(path))
                return
            
            # Get the possible letters for the current digit
            possible_letters = digit_to_letters[digits[index]]
            for letter in possible_letters:
                path.append(letter)  # Choose
                backtrack(index + 1, path)  # Explore
                path.pop()  # Unchoose (backtrack)
        
        combinations = []  # List to store all combinations
        backtrack(0, [])  # Start the recursive backtracking
        return combinations
