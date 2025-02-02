class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # To store unique characters
        left = 0  # Left pointer
        max_length = 0  # Store the maximum length

        for right in range(len(s)):  # Right pointer moves
            while s[right] in char_set:  # If duplicate, move left pointer
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])  # Add the current character
            max_length = max(max_length, right - left + 1)  # Update max length

        return max_length  # Return the maximum length found
