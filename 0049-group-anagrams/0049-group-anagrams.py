from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)  # Dictionary to store groups
        
        for word in strs:
            sorted_word = tuple(sorted(word))  # Sort word to use as key
            anagrams[sorted_word].append(word)  # Group anagrams together
        
        return list(anagrams.values())  # Return grouped anagrams
